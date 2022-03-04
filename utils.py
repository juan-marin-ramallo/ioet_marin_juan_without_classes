from datetime import datetime, timedelta
import json

#Read json file with week and weekend hour salaries
def load_work_hour_salaries():
  try:
    # Opening Work Hour Salaries JSON file
    with open('work_hour_salaries.json') as json_file:
      return json.load(json_file)
  except Exception as ex:
    raise Exception('There was a problem parsing JSON file: {0}'.format(ex))


def get_work_hour_salaries(day_worked):
  complete_work_hour_salaries = load_work_hour_salaries()

  if(day_worked == "SA" or day_worked == "SU"):
    return complete_work_hour_salaries['weekend']
  elif(day_worked == "MO" or day_worked == "TU" or day_worked == "WE" or day_worked == "TH" or day_worked == "FR"):
    return complete_work_hour_salaries['week']
  else:
    return {}

def get_next_day_worked(day_worked):
  if day_worked == "SU":
    return "MO"
  if day_worked == "MO":
    return "TU"
  if day_worked == "TU":
    return "WE"
  if day_worked == "WE":
    return "TH"
  if day_worked == "TH":
    return "FR"
  if day_worked == "FR":
    return "SA"
  if day_worked == "SA":
    return "SU"
  

def calculate_amount_to_pay_by_hour(iterate_time_worked,work_hour_salaries):
  amount_to_pay_by_hour = 0
  
  try:
    #Iterate every schedule existing in work_hour_salaries
    for schedule_to_pay, amount_to_pay in work_hour_salaries.items():
      start_time_schedule = datetime.strptime(schedule_to_pay.split("-")[0].strip(), "%H:%M")
      end_time_schedule = datetime.strptime(schedule_to_pay.split("-")[1].strip(), "%H:%M")
  
      if(end_time_schedule.hour == 0):
        end_time_schedule = end_time_schedule + timedelta(days=1)
        
      if(iterate_time_worked >= start_time_schedule and iterate_time_worked < end_time_schedule):
        amount_to_pay_by_hour = int(amount_to_pay.split(" ")[0])
        break
  except Exception as ex:
    raise Exception('There was a problem calculating amount to pay by hour worked: {0}'.format(ex))
  
  return amount_to_pay_by_hour

