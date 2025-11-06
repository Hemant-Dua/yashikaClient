import gi, time, psutil, requests, threading
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib, Gdk

from tts import yashika_speak   # your TTS module

# -------- Backend Chat Function --------
ip = input("Enter Server IP: ")
BASE_URL = "http://"+ ip +":7860"   # replace with your server IP

def stream_yashika(message, on_chunk, on_done, on_error):
    try:
        with requests.post(
            f"{BASE_URL}/chat",
            json={"message": message},
            stream=True,
            timeout=10
        ) as resp:
            resp.raise_for_status()
            for chunk in resp.iter_content(chunk_size=None):
                text = chunk.decode(errors="ignore")
                if text:
                    GLib.idle_add(on_chunk, text)
        GLib.idle_add(on_done)
    except Exception as e:
        GLib.idle_add(on_error, str(e))


# -------- Chat Window --------
class ChatWindow(Gtk.Box):
    def __init__(self, back_callback):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Back button
        back_btn = Gtk.Button(label="⬅ Back")
        back_btn.set_css_classes(["cyberButton"])
        back_btn.connect("clicked", lambda *_: back_callback())
        self.append(back_btn)

        # Chat history
        self.textview = Gtk.TextView()
        self.textview.set_editable(False)
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        self.textbuffer = self.textview.get_buffer()
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_child(self.textview)
        scrolled.set_vexpand(True)
        scrolled.set_margin_top(10)
        scrolled.set_margin_bottom(10)
        self.append(scrolled)

        # Typing indicator
        self.typing_label = Gtk.Label(label="")
        self.typing_label.set_halign(Gtk.Align.START)
        self.append(self.typing_label)

        # Input + button
        input_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Type your message...")
        self.textview.set_css_classes(["textViewChat"])
        self.entry.set_css_classes(["chatEntry"])
        self.entry.connect("activate", self.on_send)
        send_button = Gtk.Button(label="Send")
        send_button.set_css_classes(["cyberButton"])
        send_button.connect("clicked", self.on_send)
        input_box.append(self.entry)
        input_box.append(send_button)
        self.append(input_box)

        # Reusable tags with softer colors
        self.tag_you = self.textbuffer.create_tag("chatYou", foreground="#ff99ff", weight=700)  # soft magenta
        self.tag_bot = self.textbuffer.create_tag("chatBot", foreground="#66cccc")  # soft cyan/teal
        self.tag_err = self.textbuffer.create_tag("chatError", foreground="#ff6666")  # softer red

        # Streaming state
        self.bot_mark = None
        self.bot_streaming = False
        self.reply_accum = []


    def _scroll_to_end(self):
        end_iter = self.textbuffer.get_end_iter()
        self.textview.scroll_to_iter(end_iter, 0.0, True, 0.0, 1.0)

    def _append_line(self, sender, text, tag=None):
        end_iter = self.textbuffer.get_end_iter()
        self.textbuffer.insert_with_tags(end_iter, f"{sender}: {text}\n", tag)
        self._scroll_to_end()

    def _start_bot_stream(self):
        if self.bot_streaming:
            return
        end_iter = self.textbuffer.get_end_iter()
        self.textbuffer.insert_with_tags(end_iter, "Yashika: ", self.tag_bot)
        end_iter = self.textbuffer.get_end_iter()
        if self.bot_mark:
            self.textbuffer.delete_mark(self.bot_mark)
        # right-gravity mark so it stays at the end as we insert more
        self.bot_mark = self.textbuffer.create_mark("bot_end", end_iter, False)
        self.bot_streaming = True
        self._scroll_to_end()

    def _append_bot_chunk(self, text):
        if not self.bot_streaming:
            self._start_bot_stream()
        if not text:
            return
        insert_iter = self.textbuffer.get_iter_at_mark(self.bot_mark)
        self.textbuffer.insert_with_tags(insert_iter, text, self.tag_bot)
        self._scroll_to_end()

    def _end_bot_stream(self):
        if not self.bot_streaming:
            return
        end_iter = self.textbuffer.get_end_iter()
        self.textbuffer.insert(end_iter, "\n")
        self.bot_streaming = False
        self._scroll_to_end()

    def on_send(self, widget):
        msg = self.entry.get_text().strip()
        if not msg:
            return
        self.entry.set_text("")
        self._append_line("You", msg, self.tag_you)

        self.typing_label.set_text("Yashika is typing…")
        self.reply_accum = []

        def on_chunk(text):
            self.reply_accum.append(text)
            self._append_bot_chunk(text)

        def on_done():
            self._end_bot_stream()
            self.typing_label.set_text("")
            reply = "".join(self.reply_accum).strip()
            if reply:
                try:
                    yashika_speak(reply)
                except Exception:
                    pass

        def on_error(err):
            self._end_bot_stream()
            self.typing_label.set_text("")
            self._append_line("Error", err, self.tag_err)

        threading.Thread(
            target=stream_yashika,
            args=(msg, on_chunk, on_done, on_error),
            daemon=True
        ).start()


# -------- Main Dashboard --------
class YashikaUI(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="YASHIKA Client")
        self.set_default_size(800, 480)
        self.set_decorated(False)
        self.fullscreen()

        self.stack = Gtk.Stack()
        self.set_child(self.stack)

        # Dashboard Screen
        dashboard = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        dashboard.set_halign(Gtk.Align.CENTER)
        dashboard.set_valign(Gtk.Align.CENTER)
        dashboard.set_css_classes(["glassBox"])

        self.clock_label = Gtk.Label(label="00:00 AM", css_classes=["clock"])
        self.date_label = Gtk.Label(label="01 Jan, 1970", css_classes=["date"])
        self.battery_label = Gtk.Label(label="🔋 100%", css_classes=["battery"])

        dashboard.append(self.clock_label)
        dashboard.append(self.date_label)
        dashboard.append(self.battery_label)

        grid = Gtk.Grid(column_spacing=40, row_spacing=20)
        dashboard.append(grid)

        self.add_button(grid, "Chat", 0, 0, self.open_chat)
        self.add_button(grid, "Presets", 1, 0, None)
        self.add_button(grid, "Controls", 0, 1, None)
        self.add_button(grid, "Settings", 1, 1, None)

        self.stack.add_named(dashboard, "dashboard")

        # Timer
        GLib.timeout_add(1000, self.update_time)

    def add_button(self, grid, label, col, row, callback):
        btn = Gtk.Button(label=label)
        btn.set_size_request(160, 80)
        btn.set_css_classes(["cyberButton"])
        if callback:
            btn.connect("clicked", lambda *_: callback())
        grid.attach(btn, col, row, 1, 1)

    def update_time(self):
        now = time.strftime("%I:%M %p")
        today = time.strftime("%d %b, %Y")
        battery = psutil.sensors_battery()
        batt = f"{battery.percent}%" if battery and battery.percent is not None else "N/A"

        self.clock_label.set_text(now)
        self.date_label.set_text(today)
        self.battery_label.set_text(f"🔋 {batt}")
        return True

    def open_chat(self):
        chat = ChatWindow(self.show_dashboard)
        self.stack.add_named(chat, "chat")
        self.stack.set_visible_child_name("chat")

    def show_dashboard(self):
        self.stack.set_visible_child_name("dashboard")


# -------- Application --------
class YashikaApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.yashika.Client")

    def do_activate(self, *args):
        win = YashikaUI(self)
        win.present()


# -------- CSS --------
css = b"""
window {
    background: linear-gradient(135deg, #000000, #001a33);
}
.clock {
    font-size: 48px;
    color: #00FFFF;
    text-shadow: 0 0 12px #00FFFF;
}
.date {
    font-size: 24px;
    color: #AAAAAA;
}
.battery {
    font-size: 18px;
    color: #00FF88;
}
.cyberButton {
    background: black;
    color: #00FFFF;
    border: 2px solid #00FFFF;
    font-size: 20px;
    border-radius: 12px;
    transition: all 200ms ease-in-out;
}
.cyberButton:hover {
    background: #001122;
    box-shadow: 0 0 15px #00FFFF;
}
.glassBox {
    background: rgba(0, 0, 0, 0.6);
    border: 2px solid #00FFFF;
    border-radius: 12px;
    box-shadow: 0 0 20px #00FFFF;
    padding: 20px;
}
.textViewChat {
    background-color: #0d0d1a;  /* dark navy */
    color: #cccccc;             /* soft gray text */
    border-radius: 8px;
    padding: 6px;
}
.chatEntry {
    background-color: #1a1a2e;
    color: #eeeeee;
    border-radius: 6px;
    padding: 4px;
}


"""

provider = Gtk.CssProvider()
provider.load_from_data(css)
display = Gdk.Display.get_default()
if display:
    Gtk.StyleContext.add_provider_for_display(
        display,
        provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
    )

# -------- Run --------
app = YashikaApp()
app.run(None)
