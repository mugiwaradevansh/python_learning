import time

timestamp = time.strftime('%H:%M')
print(timestamp)

if timestamp <= '12:00':
    print("Good Morning")
elif '12:00' < timestamp <= '18:00':
    print("Good Afternoon")
elif timestamp > '18:00':
    print("Good Evening")