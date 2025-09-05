from datetime import datetime
import calendar
import re


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    cal = calendar.Calendar()
    weekdays = {
        calendar.MONDAY: 'Monday',
        calendar.TUESDAY: 'Tuesday',
        calendar.WEDNESDAY: 'Wednesday',
        calendar.THURSDAY: 'Thursday',
        calendar.FRIDAY: 'Friday',
        calendar.SATURDAY: 'Saturday',
        calendar.SUNDAY: 'Sunday'
    }
    monthdays = [(d[0], d[1], d[2], weekdays[d[3]]) for d in cal.itermonthdays4(year, month) if d[1] == month]
    monthdays = [d for d in monthdays if d[3] == day_of_week]
    if re.search(r'\d+', week):
        try:
            dt = monthdays[int(week[0])-1]
            return datetime.date(datetime(dt[0], dt[1], dt[2]))
        except:
            raise MeetupDayException("Out of range")
    elif week == 'last':
        dt = monthdays[-1]
        return datetime.date(datetime(dt[0], dt[1], dt[2]))
    else:
        dt = [d for d in monthdays if 13 <= d[2] <= 19]
        return datetime.date(datetime(dt[0][0], dt[0][1], dt[0][2]))
