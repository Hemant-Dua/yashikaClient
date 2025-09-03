# Generated from ./dateparse_utils.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dateparse_utilsParser import dateparse_utilsParser
else:
    from dateparse_utilsParser import dateparse_utilsParser

# This class defines a complete listener for a parse tree produced by dateparse_utilsParser.
class dateparse_utilsListener(ParseTreeListener):

    # Enter a parse tree produced by dateparse_utilsParser#parse.
    def enterParse(self, ctx:dateparse_utilsParser.ParseContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#parse.
    def exitParse(self, ctx:dateparse_utilsParser.ParseContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#dateExpr.
    def enterDateExpr(self, ctx:dateparse_utilsParser.DateExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#dateExpr.
    def exitDateExpr(self, ctx:dateparse_utilsParser.DateExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#timeExpr.
    def enterTimeExpr(self, ctx:dateparse_utilsParser.TimeExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#timeExpr.
    def exitTimeExpr(self, ctx:dateparse_utilsParser.TimeExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#singleTimeExpr.
    def enterSingleTimeExpr(self, ctx:dateparse_utilsParser.SingleTimeExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#singleTimeExpr.
    def exitSingleTimeExpr(self, ctx:dateparse_utilsParser.SingleTimeExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#twentyFourHourTimeExpr.
    def enterTwentyFourHourTimeExpr(self, ctx:dateparse_utilsParser.TwentyFourHourTimeExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#twentyFourHourTimeExpr.
    def exitTwentyFourHourTimeExpr(self, ctx:dateparse_utilsParser.TwentyFourHourTimeExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#twelveHourTimeExpr.
    def enterTwelveHourTimeExpr(self, ctx:dateparse_utilsParser.TwelveHourTimeExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#twelveHourTimeExpr.
    def exitTwelveHourTimeExpr(self, ctx:dateparse_utilsParser.TwelveHourTimeExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#ampm.
    def enterAmpm(self, ctx:dateparse_utilsParser.AmpmContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#ampm.
    def exitAmpm(self, ctx:dateparse_utilsParser.AmpmContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#singleDateExpr.
    def enterSingleDateExpr(self, ctx:dateparse_utilsParser.SingleDateExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#singleDateExpr.
    def exitSingleDateExpr(self, ctx:dateparse_utilsParser.SingleDateExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#monthDayMaybeYearExpr.
    def enterMonthDayMaybeYearExpr(self, ctx:dateparse_utilsParser.MonthDayMaybeYearExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#monthDayMaybeYearExpr.
    def exitMonthDayMaybeYearExpr(self, ctx:dateparse_utilsParser.MonthDayMaybeYearExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#dayMonthMaybeYearExpr.
    def enterDayMonthMaybeYearExpr(self, ctx:dateparse_utilsParser.DayMonthMaybeYearExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#dayMonthMaybeYearExpr.
    def exitDayMonthMaybeYearExpr(self, ctx:dateparse_utilsParser.DayMonthMaybeYearExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#yearMonthDayExpr.
    def enterYearMonthDayExpr(self, ctx:dateparse_utilsParser.YearMonthDayExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#yearMonthDayExpr.
    def exitYearMonthDayExpr(self, ctx:dateparse_utilsParser.YearMonthDayExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#nthWeekdayInMonthMaybeYearExpr.
    def enterNthWeekdayInMonthMaybeYearExpr(self, ctx:dateparse_utilsParser.NthWeekdayInMonthMaybeYearExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#nthWeekdayInMonthMaybeYearExpr.
    def exitNthWeekdayInMonthMaybeYearExpr(self, ctx:dateparse_utilsParser.NthWeekdayInMonthMaybeYearExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#firstLastWeekdayInMonthMaybeYearExpr.
    def enterFirstLastWeekdayInMonthMaybeYearExpr(self, ctx:dateparse_utilsParser.FirstLastWeekdayInMonthMaybeYearExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#firstLastWeekdayInMonthMaybeYearExpr.
    def exitFirstLastWeekdayInMonthMaybeYearExpr(self, ctx:dateparse_utilsParser.FirstLastWeekdayInMonthMaybeYearExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#specialDateMaybeYearExpr.
    def enterSpecialDateMaybeYearExpr(self, ctx:dateparse_utilsParser.SpecialDateMaybeYearExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#specialDateMaybeYearExpr.
    def exitSpecialDateMaybeYearExpr(self, ctx:dateparse_utilsParser.SpecialDateMaybeYearExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#thisNextLast.
    def enterThisNextLast(self, ctx:dateparse_utilsParser.ThisNextLastContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#thisNextLast.
    def exitThisNextLast(self, ctx:dateparse_utilsParser.ThisNextLastContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#baseAndOffsetDateExpr.
    def enterBaseAndOffsetDateExpr(self, ctx:dateparse_utilsParser.BaseAndOffsetDateExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#baseAndOffsetDateExpr.
    def exitBaseAndOffsetDateExpr(self, ctx:dateparse_utilsParser.BaseAndOffsetDateExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaDateExprRelativeToTodayImplied.
    def enterDeltaDateExprRelativeToTodayImplied(self, ctx:dateparse_utilsParser.DeltaDateExprRelativeToTodayImpliedContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaDateExprRelativeToTodayImplied.
    def exitDeltaDateExprRelativeToTodayImplied(self, ctx:dateparse_utilsParser.DeltaDateExprRelativeToTodayImpliedContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaRelativeToTodayExpr.
    def enterDeltaRelativeToTodayExpr(self, ctx:dateparse_utilsParser.DeltaRelativeToTodayExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaRelativeToTodayExpr.
    def exitDeltaRelativeToTodayExpr(self, ctx:dateparse_utilsParser.DeltaRelativeToTodayExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#nFoosFromTodayAgoExpr.
    def enterNFoosFromTodayAgoExpr(self, ctx:dateparse_utilsParser.NFoosFromTodayAgoExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#nFoosFromTodayAgoExpr.
    def exitNFoosFromTodayAgoExpr(self, ctx:dateparse_utilsParser.NFoosFromTodayAgoExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#baseDate.
    def enterBaseDate(self, ctx:dateparse_utilsParser.BaseDateContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#baseDate.
    def exitBaseDate(self, ctx:dateparse_utilsParser.BaseDateContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#baseAndOffsetTimeExpr.
    def enterBaseAndOffsetTimeExpr(self, ctx:dateparse_utilsParser.BaseAndOffsetTimeExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#baseAndOffsetTimeExpr.
    def exitBaseAndOffsetTimeExpr(self, ctx:dateparse_utilsParser.BaseAndOffsetTimeExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#baseTime.
    def enterBaseTime(self, ctx:dateparse_utilsParser.BaseTimeContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#baseTime.
    def exitBaseTime(self, ctx:dateparse_utilsParser.BaseTimeContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaPlusMinusExpr.
    def enterDeltaPlusMinusExpr(self, ctx:dateparse_utilsParser.DeltaPlusMinusExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaPlusMinusExpr.
    def exitDeltaPlusMinusExpr(self, ctx:dateparse_utilsParser.DeltaPlusMinusExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaNextLast.
    def enterDeltaNextLast(self, ctx:dateparse_utilsParser.DeltaNextLastContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaNextLast.
    def exitDeltaNextLast(self, ctx:dateparse_utilsParser.DeltaNextLastContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaPlusMinusTimeExpr.
    def enterDeltaPlusMinusTimeExpr(self, ctx:dateparse_utilsParser.DeltaPlusMinusTimeExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaPlusMinusTimeExpr.
    def exitDeltaPlusMinusTimeExpr(self, ctx:dateparse_utilsParser.DeltaPlusMinusTimeExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#countUnitsBeforeAfterTimeExpr.
    def enterCountUnitsBeforeAfterTimeExpr(self, ctx:dateparse_utilsParser.CountUnitsBeforeAfterTimeExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#countUnitsBeforeAfterTimeExpr.
    def exitCountUnitsBeforeAfterTimeExpr(self, ctx:dateparse_utilsParser.CountUnitsBeforeAfterTimeExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#fractionBeforeAfterTimeExpr.
    def enterFractionBeforeAfterTimeExpr(self, ctx:dateparse_utilsParser.FractionBeforeAfterTimeExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#fractionBeforeAfterTimeExpr.
    def exitFractionBeforeAfterTimeExpr(self, ctx:dateparse_utilsParser.FractionBeforeAfterTimeExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaUnit.
    def enterDeltaUnit(self, ctx:dateparse_utilsParser.DeltaUnitContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaUnit.
    def exitDeltaUnit(self, ctx:dateparse_utilsParser.DeltaUnitContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaTimeUnit.
    def enterDeltaTimeUnit(self, ctx:dateparse_utilsParser.DeltaTimeUnitContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaTimeUnit.
    def exitDeltaTimeUnit(self, ctx:dateparse_utilsParser.DeltaTimeUnitContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaBeforeAfter.
    def enterDeltaBeforeAfter(self, ctx:dateparse_utilsParser.DeltaBeforeAfterContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaBeforeAfter.
    def exitDeltaBeforeAfter(self, ctx:dateparse_utilsParser.DeltaBeforeAfterContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaTimeBeforeAfter.
    def enterDeltaTimeBeforeAfter(self, ctx:dateparse_utilsParser.DeltaTimeBeforeAfterContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaTimeBeforeAfter.
    def exitDeltaTimeBeforeAfter(self, ctx:dateparse_utilsParser.DeltaTimeBeforeAfterContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#monthExpr.
    def enterMonthExpr(self, ctx:dateparse_utilsParser.MonthExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#monthExpr.
    def exitMonthExpr(self, ctx:dateparse_utilsParser.MonthExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#year.
    def enterYear(self, ctx:dateparse_utilsParser.YearContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#year.
    def exitYear(self, ctx:dateparse_utilsParser.YearContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#specialDate.
    def enterSpecialDate(self, ctx:dateparse_utilsParser.SpecialDateContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#specialDate.
    def exitSpecialDate(self, ctx:dateparse_utilsParser.SpecialDateContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#dayOfMonth.
    def enterDayOfMonth(self, ctx:dateparse_utilsParser.DayOfMonthContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#dayOfMonth.
    def exitDayOfMonth(self, ctx:dateparse_utilsParser.DayOfMonthContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#firstOrLast.
    def enterFirstOrLast(self, ctx:dateparse_utilsParser.FirstOrLastContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#firstOrLast.
    def exitFirstOrLast(self, ctx:dateparse_utilsParser.FirstOrLastContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#nth.
    def enterNth(self, ctx:dateparse_utilsParser.NthContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#nth.
    def exitNth(self, ctx:dateparse_utilsParser.NthContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#unsignedInt.
    def enterUnsignedInt(self, ctx:dateparse_utilsParser.UnsignedIntContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#unsignedInt.
    def exitUnsignedInt(self, ctx:dateparse_utilsParser.UnsignedIntContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#deltaTimeFraction.
    def enterDeltaTimeFraction(self, ctx:dateparse_utilsParser.DeltaTimeFractionContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#deltaTimeFraction.
    def exitDeltaTimeFraction(self, ctx:dateparse_utilsParser.DeltaTimeFractionContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#specialTimeExpr.
    def enterSpecialTimeExpr(self, ctx:dateparse_utilsParser.SpecialTimeExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#specialTimeExpr.
    def exitSpecialTimeExpr(self, ctx:dateparse_utilsParser.SpecialTimeExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#specialTime.
    def enterSpecialTime(self, ctx:dateparse_utilsParser.SpecialTimeContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#specialTime.
    def exitSpecialTime(self, ctx:dateparse_utilsParser.SpecialTimeContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#dayName.
    def enterDayName(self, ctx:dateparse_utilsParser.DayNameContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#dayName.
    def exitDayName(self, ctx:dateparse_utilsParser.DayNameContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#monthName.
    def enterMonthName(self, ctx:dateparse_utilsParser.MonthNameContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#monthName.
    def exitMonthName(self, ctx:dateparse_utilsParser.MonthNameContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#monthNumber.
    def enterMonthNumber(self, ctx:dateparse_utilsParser.MonthNumberContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#monthNumber.
    def exitMonthNumber(self, ctx:dateparse_utilsParser.MonthNumberContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#hour.
    def enterHour(self, ctx:dateparse_utilsParser.HourContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#hour.
    def exitHour(self, ctx:dateparse_utilsParser.HourContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#minute.
    def enterMinute(self, ctx:dateparse_utilsParser.MinuteContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#minute.
    def exitMinute(self, ctx:dateparse_utilsParser.MinuteContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#second.
    def enterSecond(self, ctx:dateparse_utilsParser.SecondContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#second.
    def exitSecond(self, ctx:dateparse_utilsParser.SecondContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#micros.
    def enterMicros(self, ctx:dateparse_utilsParser.MicrosContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#micros.
    def exitMicros(self, ctx:dateparse_utilsParser.MicrosContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#ddiv.
    def enterDdiv(self, ctx:dateparse_utilsParser.DdivContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#ddiv.
    def exitDdiv(self, ctx:dateparse_utilsParser.DdivContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#tdiv.
    def enterTdiv(self, ctx:dateparse_utilsParser.TdivContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#tdiv.
    def exitTdiv(self, ctx:dateparse_utilsParser.TdivContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#dtdiv.
    def enterDtdiv(self, ctx:dateparse_utilsParser.DtdivContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#dtdiv.
    def exitDtdiv(self, ctx:dateparse_utilsParser.DtdivContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#tddiv.
    def enterTddiv(self, ctx:dateparse_utilsParser.TddivContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#tddiv.
    def exitTddiv(self, ctx:dateparse_utilsParser.TddivContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#tzExpr.
    def enterTzExpr(self, ctx:dateparse_utilsParser.TzExprContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#tzExpr.
    def exitTzExpr(self, ctx:dateparse_utilsParser.TzExprContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#ntz.
    def enterNtz(self, ctx:dateparse_utilsParser.NtzContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#ntz.
    def exitNtz(self, ctx:dateparse_utilsParser.NtzContext):
        pass


    # Enter a parse tree produced by dateparse_utilsParser#ltz.
    def enterLtz(self, ctx:dateparse_utilsParser.LtzContext):
        pass

    # Exit a parse tree produced by dateparse_utilsParser#ltz.
    def exitLtz(self, ctx:dateparse_utilsParser.LtzContext):
        pass



del dateparse_utilsParser