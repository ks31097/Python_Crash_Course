import time
from datetime import datetime, timedelta

# Get the current time
current_time = time.time()
print("Current Time (timestanp):", current_time)

# Convert timestamp to a readible format
readable_time = datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
print("Current Time (readable):", readable_time)

# Calculate the time 5 hours from now
future_time = datetime.now() + timedelta(hours=5)
print("Time 5 hours from now:", future_time.strftime('%Y-%m-%d %H:%M:%S'))

# Calculate the time 5 hours ago
future_time = datetime.now() - timedelta(hours=5)
print("Time 5 hours from now:", future_time.strftime('%Y-%m-%d %H:%M:%S'))