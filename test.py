from datetime import datetime

s = '2021-03-26T15:00:59.5684898Z'
print(datetime.fromisoformat(s).strftime("%Y"))