
from datetime import *

date_time = datetime.now()
date_today = f"{date_time.day}/{date_time.month}/{date_time.year}"

print(date_time.strftime('%I:%M:%S %p'))