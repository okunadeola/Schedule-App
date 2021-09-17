import datetime as dt
from playsound import playsound

# # reminder
task_note = []
while True:
  print("""---------Reminder---------------

  input the options
  1. add task
  2. turn alarm on
  3. exit
  """)
  try:
    answer = int(input(">>> "))

    if answer == 1:
      task = input("input task e.g read book >>>")
      while True:
        time = input("input time e.g 02:50:00:PM >>>")
        if ":" in time:
          task_note.append([task,time])
          print(f"all task {task_note}")
          break
        else:
          print("invalid time")

    elif answer == 2:
      while True:
        for x in task_note:
            alarm_time = x[1].split(':')
            time = dt.datetime.now()
            if time.strftime("%I") == alarm_time[0] and time.strftime("%M") == alarm_time[1] and time.strftime("%S") == alarm_time[2] and time.strftime("%p") == alarm_time[3]:
              print(f"({x[1]})It is time to - {x[0]}")
              playsound("Kalimba.mp3")
        
          
    elif answer == 3:
      print("see you soon!")
      break
  except:
    print("something went wrong. try again")