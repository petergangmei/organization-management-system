import pytz
import datetime


def get_datetime_from_timestamp(timestamp):
    utc_datetime = datetime.datetime.utcfromtimestamp(timestamp)
    india_timezone = pytz.timezone('Asia/Kolkata')
    ist_datetime = utc_datetime.replace(tzinfo=pytz.UTC).astimezone(india_timezone)
    return ist_datetime