import sys, time, os

timeToCheck = int(sys.argv[1])
bradsWillToLive = -10

while not bradsWillToLive > 1:
  os.system("python main.py " + sys.argv[2])
  time.sleep(timeToCheck) #sleep for X seconds. Let's not max that CPU out!
