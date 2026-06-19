import time
from datetime import datetime
from datetime import timedelta

datetime_now = datetime.now()
print(datetime_now)

date_minus_hour = datetime_now - timedelta(hours=1)
print(date_minus_hour)

datetime_minus_hour_reformat = date_minus_hour.strftime('%Y-%m-%d %H:%M:%S')
print(datetime_minus_hour_reformat)

epoch = datetime_now.timestamp()
print(epoch)

ts_epoch = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
print(ts_epoch)