from datetime import datetime, timedelta
import utils

def calculate_pay_by_employee(employee_job_schedule):
  #Get name and schedule_worked from employee
  try:
    employee = str(employee_job_schedule.split("=")[0])
    schedule_worked = employee_job_schedule.split("=")[1].split(",")
  except Exception as ex:
    raise Exception('There was a problem reading employee job schedule {0}: {1}'.format(employee_job_schedule,ex))

  #Initialize total to pay to employee 
  total_to_pay = 0

  #Iterate for every day worked indicated in schedule
  for day_time_worked in schedule_worked:
    #Get the day and time worked from the day_time_worked
    try:
      #Check if day_time_worked length is exactly 13 characters. Example: FR23:30-00:45
      if(len(day_time_worked) != 13):
        raise Exception('The length to describe day and time worked is incorrect') 
      day_worked = str(day_time_worked[:2])
      time_worked = str(day_time_worked[-11:])
    except Exception as ex:
      raise Exception('There was a problem extracting day and time worked {0}: {1}'.format(day_time_worked,ex))

    #Get the dictionary with work hour salaries according to day_worked
    work_hour_salaries = utils.get_work_hour_salaries(day_worked)
      
    if not work_hour_salaries:
      print("The day %s is not a valid day. Please check input data" % day_worked)
      break

    #Obtain start_time_worked and end_time_worked from employee time_worked
    try:
      start_time_worked = datetime.strptime(time_worked.split("-")[0], "%H:%M")
      end_time_worked = datetime.strptime(time_worked.split("-")[1], "%H:%M")
    except Exception as ex:
      raise Exception('There was a problem extacting start and end time worked {0}: {1}'.format(time_worked,ex))
      
    #Add 1 minute to make match with start time from work_hour_salaries
    if(start_time_worked.minute == 0):
      iterate_time_worked = start_time_worked + timedelta(minutes=1)
    else:
      iterate_time_worked = start_time_worked

    #Add 1 day to end_time_worked if it is equal to zero
    if(end_time_worked.hour == 0):
      end_time_worked = end_time_worked + timedelta(days=1)

    #Iterate every hour worked for each day_worked
    while(iterate_time_worked < end_time_worked): 
      amount_to_pay_by_hour = utils.calculate_amount_to_pay_by_hour(iterate_time_worked,work_hour_salaries)

      if amount_to_pay_by_hour > 0:
        total_to_pay = total_to_pay + amount_to_pay_by_hour

      #Add 1 hora to iterate_time_worked to continue to the next hour worked
      iterate_time_worked = iterate_time_worked + timedelta(hours=1)      

    #Validate if the minute of end_time_worked is greater than 0 to pay extra hour
    if(end_time_worked.minute > 0):
      iterate_time_worked = end_time_worked

      #Validate if the hour is equal 0 to get the next day and the work_hour_salaries for this next day
      if(end_time_worked.hour == 0):
        iterate_time_worked = end_time_worked - timedelta(days=1)
        next_day_worked = utils.get_next_day_worked(day_worked)
        work_hour_salaries = utils.get_work_hour_salaries(next_day_worked)

      #Calculate the amount to pay according to iterate_time_worked and work_hour_salaries
      amount_to_pay_by_hour = utils.calculate_amount_to_pay_by_hour(iterate_time_worked,work_hour_salaries)

      if amount_to_pay_by_hour > 0:
        total_to_pay = total_to_pay + amount_to_pay_by_hour

  print("The amount to pay %s is: %d USD" %(employee,total_to_pay))

if __name__ == "__main__":
  try:  
    #calculate_pay_by_employee("KARLA=TH00:00-00:01")
    with open('job_schedule.txt') as job_schedule_file:
      for job_schedule_line in job_schedule_file:
        calculate_pay_by_employee(job_schedule_line.replace("\n", ""))
  except Exception as ex:
    print("Error catched: {0}".format(ex))

  

                                                                                                                #Iterate #  #  try:
#    
#  except Exception as ex:
#    print("Error catched: {0}".format(ex))
