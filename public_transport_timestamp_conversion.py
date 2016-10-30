import datetime
import pytz

# This method converts operation_date, publictransport timestamp + timezone
# in a datetime object.
def get_datetime(operation_date, pt_timestamp, timezone):
    year, month, day = map(int, operation_date.split("-"))
    hour, minute, second = map(int, pt_timestamp.split(":"))

    start_operation_date = datetime.timedelta(hours = 4)
    pt_datetime = datetime.timedelta(hours = hour, minutes = minute, seconds = second)

    local_time = pytz.timezone(timezone)
    timestamp = local_time.localize(
        datetime.datetime(year, month, day, 4, 0)) - start_operation_date
    timestamp = timestamp + pt_datetime
    return timestamp
