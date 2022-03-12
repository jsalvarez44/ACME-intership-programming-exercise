__author__ = 'jsalvarez44'


# Function to show every employee in the employees list sended as a parameter.
def show_employees(employees):
    # We iterate over the list of employees.
    for employee in employees:
        # Create a string varable, starts with the name of the employee.
        str_employee_data = f'{employee.name}='
        
        # We iterate over the employee records.
        for date_time in employee.record:
            # We add to the string variable the day of the date_time object.
            str_employee_data += f'{date_time.day}'
            
            # We validate leading zeros to optimally format the printout by comparing if the hour or minute of the entrance 
            # time is less than 10, then a leading zero is added to it.
            if date_time.entrance_time.hours < 10:
                str_employee_data += f'0{date_time.entrance_time.hours}:'
            else:
                str_employee_data += f'{date_time.entrance_time.hours}:'
            if date_time.entrance_time.minutes < 10:
                str_employee_data += f'0{date_time.entrance_time.minutes}-'
            else:
                str_employee_data += f'{date_time.entrance_time.minutes}-'

            # We validate leading zeros to optimally format the printout by comparing if the hour or minute of the departure 
            # time is less than 10, then a leading zero is added to it.
            if date_time.departure_time.hours < 10:
                str_employee_data += f'0{date_time.departure_time.hours}:'
            else:
                str_employee_data += f'{date_time.departure_time.hours}:'
            if date_time.departure_time.minutes < 10:
                str_employee_data += f'0{date_time.departure_time.minutes}'
            else:
                str_employee_data += f'{date_time.departure_time.minutes}'
                
            # We add a ',' at le end of the string variable to give it the correct formatting.
            str_employee_data += ','
        
        # We print the string variable to show the information about every employee.
        print(str_employee_data[:-1])


# Function to show the final output receiving a list of results as a parameter.
def show_output(results):
    for result in results:
        print(result)
