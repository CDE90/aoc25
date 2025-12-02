import datetime
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

day, year = None, None

# Read command line arguments for day and year (if provided)
if len(sys.argv) > 1:
    day = int(sys.argv[1])
if len(sys.argv) > 2:
    year = int(sys.argv[2])

# If day or year not provided, use today's date
if day is None:
    day = datetime.date.today().day
if year is None:
    year = datetime.date.today().year

day_fmt = str(day).zfill(2)

# Check if the day directory exists
if os.path.exists(day_fmt):
    print(f"Day {day} already exists")
    sys.exit(1)

# Get the template file
with open("template.py") as f:
    template = f.read()

# Get the input from the AoC website
url = f"https://adventofcode.com/{year}/day/{day}/input"

session = os.getenv("AOC_SESSION")
if session is None:
    print("AOC_SESSION environment variable not set")
    sys.exit(1)

assert session is not None
response = requests.get(url, cookies={"session": session})
input = response.text

# Create a new directory for the day
os.mkdir(day_fmt)

# Create a new files for the input and test
with open(f"{day_fmt}/inp.txt", "w") as f:
    f.write(input)

with open(f"{day_fmt}/test.txt", "w") as f:
    f.write("")

# Create a new file for the code
with open(f"{day_fmt}/sol.py", "w") as f:
    f.write(template.replace("{{day}}", day_fmt))

print(f"Created day {day}")
