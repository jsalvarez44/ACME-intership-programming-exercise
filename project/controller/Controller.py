__author__ = 'jsalvarez44'

# Importing model, view and DAO
from model.Model import Time, DateTime, Employee
from view.View import show_employees, show_output
import model.DAO as DAO


# Function to create & return an objects list of type Employee from the reading and processing of the data by the DAO functions.
def create_employees_from_data():
    # Result of reading and processing the data by the DAO functions.
    names, schedules = DAO.read_data()

    # List of employees, starts empty.
    employees = []

    # We iterate over the lists of names and schedules from the length of the names because they have the same size.
    for i in range(len(names)):
        # Saving the employee name into a variable
        name = names[i]

        # Creating the employee record, starts empty.
        record = []

        # We iterate over the schedules to create the employee record
        for raw_datetime in schedules[i]:
            # We know that the day is in the first two positions of the raw_datetime, so we split that string in substrings.
            try:
                day = raw_datetime[:2]
                raw_time = raw_datetime[2:]
            except:
                print('Error while spliting day & time data.')

            # We split the schedule by the '-' to get the entrance time & the departure_time.
            try:
                splitted_time = raw_time.split('-')
                raw_entrance_time = splitted_time[0]
                raw_departure_time = splitted_time[1]
            except:
                print('Error while splitting the entrance & departure time')

            # We split the entrance time by the ':' to get the hours & minutes of the entrance time.
            try:
                splitted_entrance_time = raw_entrance_time.split(':')
                entrance_hours = int(splitted_entrance_time[0])
                entrance_minutes = int(splitted_entrance_time[1])
            except:
                print('Error while splitting the hours & minutes of the entrance time')

            # We split the departure time by the ':' to get the hours & minutes of the departure time.
            try:
                splitted_departure_time = raw_departure_time.split(':')
                departure_hours = int(splitted_departure_time[0])
                departure_minutes = int(splitted_departure_time[1])
            except:
                print('Error while splitting the hours & minutes of the departure time')

            # We create the entrance_time & departure_time objects.
            entrance_time = Time(entrance_hours, entrance_minutes)
            departure_time = Time(departure_hours, departure_minutes)

            # We create the date_time object with the day of the schedule, the entrace_time & the departure_time fields.
            date_time = DateTime(day, entrance_time, departure_time)

            # We save the date_time object in the record list.
            record.append(date_time)

        # We create the new_employee object with the name of the employee & the record list.
        new_employee = Employee(name, record)
        
        # We save the new_employee object in the employees list.
        employees.append(new_employee)

    # Uncomment to print the employees list.
    #show_employees(employees)

    return employees


# Function to process the employees data for an object listing to show a table containing pairs of employees & how often they have 
# coincided in the office at the same day & time.
def process_employees_data(employees):
    # Create the list of results, starts empty.
    results = []
        
    # We iterate with a double for to get all the posibilities of pairs without repetitions. 
    for i in range(len(employees)):
        
        for j in range(i+1, len(employees)):
            # Start the match counter at 0
            match_counter = 0
            
            # We save the names of the pair of employees in a variable called str_result.
            str_result = f'{employees[i].name}-{employees[j].name}: '
            
            # Starts another double for to compare the records of the two employees at positions i & j to find a pair.
            for employee_i_record in employees[i].record:
                for employee_j_record in employees[j].record:
                    
                    # Compare if the day of the record is equals to the two employees.
                    if employee_i_record.day == employee_j_record.day:
                        # Use the 'compare' function to return an integer value to the entrance & departure comparations variables.
                        entrance_comparation = employee_j_record.entrance_time.compare(employee_i_record.entrance_time)
                        departure_comparation = employee_j_record.departure_time.compare(employee_i_record.departure_time)
                    
                        # We carry out the necessary comparisons, if there is a match, the counter will be incremented by one.
                        if(entrance_comparation == -1 or entrance_comparation == 0) and (departure_comparation == 1 or departure_comparation == 0):
                            match_counter += 1
                        elif(entrance_comparation == -1 or entrance_comparation == 0) and (departure_comparation == -1):
                            temporal_comparation = employee_i_record.entrance_time.compare(employee_j_record.departure_time)
                            if temporal_comparation == -1:
                                match_counter += 1
                        elif(entrance_comparation == 1) and (departure_comparation == 1 or departure_comparation == 0):
                            temporal_comparation = employee_j_record.entrance_time.compare(employee_i_record.departure_time)
                            if temporal_comparation == -1:
                                match_counter += 1
                        elif(entrance_comparation == 1) and (departure_comparation == -1):
                            temporal_comparation = employee_j_record.entrance_time.compare(employee_j_record.departure_time)
                            if temporal_comparation == -1:
                                match_counter += 1

            # We add the match_counter value conerted into string to the str_result variable & append it to the results list.
            str_result += str(match_counter)
            results.append(str_result)
    
    return results

# Function to start the view in the main to show the results.
def start_view():
    employees = create_employees_from_data()
    results = process_employees_data(employees)
    show_output(results)
