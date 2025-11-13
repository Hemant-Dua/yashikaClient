import gi, time, psutil, requests, threading, collections
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
        self.set_halign(Gtk.Align.FILL)
        self.set_valign(Gtk.Align.FILL)

        # Wrap everything in a "glassBox" container
        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container.set_css_classes(["glassBox"])
        container.set_margin_top(10)
        container.set_margin_bottom(10)
        container.set_margin_start(10)
        container.set_margin_end(10)
        self.append(container)

        # Back button
        back_btn = Gtk.Button(label="⬅ Back")
        back_btn.set_css_classes(["cyberButton"])
        back_btn.connect("clicked", lambda *_: back_callback())
        container.append(back_btn)

        # Chat history
        self.textview = Gtk.TextView()
        self.textview.set_editable(False)
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        self.textview.set_css_classes(["textViewChat"])
        self.textbuffer = self.textview.get_buffer()
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_child(self.textview)
        scrolled.set_vexpand(True)
        container.append(scrolled)

        # Typing indicator
        self.typing_label = Gtk.Label(label="")
        self.typing_label.set_halign(Gtk.Align.START)
        container.append(self.typing_label)

        # Input + button
        input_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Type your message...")
        self.entry.set_css_classes(["chatEntry"])
        self.entry.set_hexpand(True)
        self.entry.connect("activate", self.on_send)
        send_button = Gtk.Button(label="Send")
        send_button.set_css_classes(["cyberButton"])
        send_button.connect("clicked", self.on_send)
        input_box.append(self.entry)
        input_box.append(send_button)
        container.append(input_box)

        # Reusable tags with softer colors
        self.tag_you = self.textbuffer.create_tag(
            "chatYou",
            foreground="#ff99ff",
            weight=700,
            size_points=16  # 👈 font size for your text
        )
        self.tag_bot = self.textbuffer.create_tag(
            "chatBot",
            foreground="#66cccc",
            size_points=16  # 👈 same for Yashika
        )
        self.tag_err = self.textbuffer.create_tag(
            "chatError",
            foreground="#ff6666",
            weight=600,
            size_points=15
        )


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

        self.typing_label.set_markup('<span foreground="white" size="16000">Yashika is typing…</span>')
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


# -------- Presets Window --------
class PresetsWindow(Gtk.Box):
    def __init__(self, back_callback):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_halign(Gtk.Align.FILL)
        self.set_valign(Gtk.Align.FILL)

        # Outer glass box
        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container.set_css_classes(["glassBox"])
        container.set_margin_top(10)
        container.set_margin_bottom(10)
        container.set_margin_start(10)
        container.set_margin_end(10)
        self.append(container)

        # Back button
        back_btn = Gtk.Button(label="⬅ Back")
        back_btn.set_css_classes(["cyberButton"])
        back_btn.connect("clicked", lambda *_: back_callback())
        container.append(back_btn)

        # Scrollable preset area
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_vexpand(True)
        scrolled.set_hexpand(True)
        container.append(scrolled)

        # Grid layout for buttons
        grid = Gtk.Grid(column_spacing=20, row_spacing=20)
        grid.set_halign(Gtk.Align.CENTER)
        grid.set_valign(Gtk.Align.START)
        grid.set_margin_top(10)
        scrolled.set_child(grid)

        # Preset names
        presets = [
            "Developer Mode",
            "Study Mode",
            "Gaming Mode",
            "Chill Mode",
            "Problem Solving / DSA Mode",
            "Project Mode"
        ]

        # Add buttons in a 2-column grid
        cols = 2
        for i, name in enumerate(presets):
            button = Gtk.Button(label=name)
            button.set_css_classes(["cyberButton"])
            button.set_size_request(250, 100)  # 👈 wearable-friendly box size
            button.connect("clicked", lambda _, n=name: self.activate_preset(n))

            row, col = divmod(i, cols)
            grid.attach(button, col, row, 1, 1)

    def activate_preset(self, preset_name):
        print(f"Activating preset: {preset_name}")
        preset_map = {
            "Developer Mode": [
                "open vs code",
                "open chrome",
                "open github",
                "open projects"
            ],
            "Study Mode": [
                "open chatgpt",
                "open youtube",
            ],
            "Gaming Mode": [
                "open steam",
            ],
            "Chill Mode": [
                "open youtube",
            ],
            "Problem Solving / DSA Mode": [
                "open vs code",
                "open leetcode",
                "open chatgpt"
            ],
            "Project Mode": [
                "open vs code",
                "open projects",
                "open github",
                "open notepad"
            ]
        }

        tasks = preset_map.get(preset_name, [])
        if not tasks:
            print(f"No tasks for preset: {preset_name}")
            return

        def run_tasks():
            for msg in tasks:
                try:
                    print(f"Sending: {msg}")
                    requests.post(f"{BASE_URL}/chat", json={"message": msg}, timeout=10)
                    time.sleep(1.2)
                except Exception as e:
                    print(f"Error sending preset command: {e}")

        threading.Thread(target=run_tasks, daemon=True).start()

# -------- Network Window --------
class NetworkWindow(Gtk.Box):
    def __init__(self, back_callback):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.set_css_classes(["glassBox", "networkPage"])
        self.set_margin_top(10)
        self.set_margin_bottom(10)
        self.set_margin_start(10)
        self.set_margin_end(10)

        self.back_callback = back_callback

        # Back button
        btn = Gtk.Button(label="⬅ Back")
        btn.set_css_classes(["cyberButton"])
        btn.connect("clicked", lambda *_: back_callback())
        self.append(btn)

        # Main metrics
        self.health = Gtk.Label(label="Health: --")
        self.uptime = Gtk.Label(label="Uptime: --:--:--")
        self.lat_label = Gtk.Label(label="Latency: -- ms")

        # Sparkline (kept exact as you want)
        self.sparkline = Gtk.Label(label="...")
        self.sparkline.set_css_classes(["sparkline"])

        # CPU/RAM bars
        self.cpu_bar = Gtk.ProgressBar()
        self.cpu_bar.set_show_text(False)

        self.ram_bar = Gtk.ProgressBar()
        self.ram_bar.set_show_text(False)

        # FIXED — wrap bars so width actually applies
        cpu_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cpu_box.set_size_request(300, -1)
        cpu_box.set_halign(Gtk.Align.CENTER)
        cpu_box.append(self.cpu_bar)

        ram_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        ram_box.set_size_request(300, -1)
        ram_box.set_halign(Gtk.Align.CENTER)
        ram_box.append(self.ram_bar)

        # Layout container
        col = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)

        col.append(self.health)
        col.append(self.uptime)
        col.append(self.lat_label)

        # Proper titled section
        lat_title = Gtk.Label(label="Latency Trend")
        lat_title.set_css_classes(["title"])
        col.append(lat_title)
        col.append(self.sparkline)

        cpu_title = Gtk.Label(label="CPU Usage")
        cpu_title.set_css_classes(["title"])
        col.append(cpu_title)
        col.append(cpu_box)

        ram_title = Gtk.Label(label="RAM Usage")
        ram_title.set_css_classes(["title"])
        col.append(ram_title)
        col.append(ram_box)

        self.append(col)

        # Data
        self.history = collections.deque(maxlen=20)
        self.start_time = time.time()

        GLib.timeout_add(1000, self.update_metrics)

    def update_metrics(self):
        # Ping
        try:
            t = time.time()
            requests.get(f"{BASE_URL}/ping", timeout=1)
            lat = int((time.time() - t) * 1000)
        except:
            lat = None

        # Health
        if lat is None:
            self.health.set_text("Health: ❌ DOWN")
        elif lat < 100:
            self.health.set_text(f"Health: 🟢 {lat} ms")
        elif lat < 300:
            self.health.set_text(f"Health: 🟡 {lat} ms")
        else:
            self.health.set_text(f"Health: 🔴 {lat} ms")


        # Uptime
        e = int(time.time() - self.start_time)
        h, m, s = e//3600, (e%3600)//60, e%60
        self.uptime.set_text(f"Uptime: {h:02}:{m:02}:{s:02}")

        # Latency text
        self.lat_label.set_text(f"Latency: {lat if lat else 'N/A'} ms")

        # History
        self.history.append(lat if lat else 1000)

        # 🔥 Unicode latency bar (as you want)
        blocks = "▁▂▃▄▅▆▇█"
        scaled = ""
        max_val = max(self.history) if self.history else 1

        for v in self.history:
            level = int((v / max_val) * (len(blocks) - 1))
            scaled += blocks[level]

        self.sparkline.set_text(scaled)

        # Local CPU/RAM
        self.cpu_bar.set_fraction(psutil.cpu_percent() / 100.0)
        self.ram_bar.set_fraction(psutil.virtual_memory().percent / 100.0)

        return True

# -------- Main Dashboard --------
class YashikaUI(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="YASHIKA Client")
        self.set_default_size(800, 480)
        self.set_decorated(False)
        self.fullscreen()

        self.stack = Gtk.Stack()
        self.set_child(self.stack)

        # ---------------- Dashboard Screen ----------------
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

        # Buttons
        self.add_button(grid, "Chat", 0, 0, self.open_chat)
        self.add_button(grid, "Presets", 1, 0, self.show_presets)
        self.add_button(grid, "Network", 0, 1, self.open_network)
        self.add_button(grid, "Settings", 1, 1, None)

        self.stack.add_named(dashboard, "dashboard")
        # ---------------- End Dashboard ----------------

        # Timer
        GLib.timeout_add(1000, self.update_time)

    # ---------------- Helper Functions ----------------
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

    # ---------------- Navigation ----------------
    def open_chat(self):
        if not hasattr(self, "chat_page"):
            self.chat_page = ChatWindow(self.show_dashboard)
            self.stack.add_named(self.chat_page, "chat")
        self.stack.set_visible_child_name("chat")
    
    def show_presets(self):
        if not hasattr(self, "presets_page"):
            self.presets_page = PresetsWindow(self.show_dashboard)
            self.stack.add_named(self.presets_page, "presets")
        self.stack.set_visible_child_name("presets")

    def open_network(self):
        if not hasattr(self, "network_page"):
            self.network_page = NetworkWindow(self.show_dashboard)
            self.stack.add_named(self.network_page, "network")
        self.stack.set_visible_child_name("network")

    def show_dashboard(self):
        self.stack.set_visible_child_name("dashboard")

# -------- Application --------
class YashikaApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.yashika.Client")

    def do_activate(self, *args):
        win = YashikaUI(self)
        win.present()

#----------CSS Provider---------
provider = Gtk.CssProvider()
provider.load_from_path("themes/default.css")
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
