#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    sys.exit("Usage:: " + sys.argv[0] + " nic_number")

nic = str(sys.argv[1]);

if len(nic) != 10 and len(nic) != 12:
    sys.exit("[x] Error:: Wrong nic provided")

if (len(nic) == 10 and (nic[-1] != "v" and nic[-1] != "V" and nic[-1] != "x" and nic[-1] != "X")):
    sys.exit("[x] Error:: Wrong nic provided x")


months = {
        "January": 31,
        "February": 29,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
        }
total_days_passed = 0

birth_year = 0
birth_month = 0
birth_date = 0
g_clc = 0
gender = 0


if(len(nic) == 10):
    birth_year = "19" + nic[0:2]
    g_clc = int(nic[2:5])
elif(len(nic) == 12):
    birth_year = nic[0:4]
    g_clc = int(nic[4: 7])

if(g_clc > 500):
    gender = "Female"
    g_clc = g_clc - 500
else:
    gender = "Male"


for month in months: 
    total_days_passed = total_days_passed + int(months[month])
    if(g_clc <= total_days_passed):
        birth_month = month
        birth_date = g_clc - total_days_passed + months[month]
        break

print("NIC No   :: " + str(nic))
print("Birthday :: " + str(birth_year) + "-" + str(birth_month) + "-" + str(birth_date));
print("Gender   :: " + str(gender))


