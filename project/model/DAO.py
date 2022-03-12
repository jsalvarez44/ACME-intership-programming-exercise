__author__ = 'jsalvarez44'


# Function to load the employees data from the employees_schedule_data file.
def load_employees_data():
    raw_listing = []

    try:
        # We open the employees_schedule_data file & save the information in a list.
        employees_schedule_archive = open('data/employees_schedule_data.txt', 'r')
        raw_listing = employees_schedule_archive.readlines()
        employees_schedule_archive.close()
    except:
        print('Error while loading data')

    return raw_listing


# Function to clean the employees data after processing it.
def clean_employees_data(raw_listing):
    cleaned_listing = []

    try:
        # We iterate over the listing & replace every '\n' with a '' to clean to data.
        for schedules in raw_listing:
            cleaned_schedules = schedules.replace('\n', '')
            cleaned_listing.append(cleaned_schedules)
    except:
        print('Error while cleaning data')

    return cleaned_listing


# Function to split the data into two lists. names & schedules
def split_data_in_name_and_schedule(listing):
    names = []
    raw_schedules = []

    try:
        # We iterate over the listing & split every '=' according to the format.
        for schedules in listing:
            splitted_schedule = schedules.split('=')
            
            # We append the names & schedules into their lists respectively.
            names.append(splitted_schedule[0])
            raw_schedules.append(splitted_schedule[1])
    except:
        print('Error while spliting data')

    return names, raw_schedules


# Function to convert a string variable of raw schedules into a list.
def raw_schedules_to_listing(raw_schedules):
    list_schedules = []

    try:
        # We iterate over the raw schedules & split every ',' according to the format.
        for raw_schedule in raw_schedules:
            splitted_schedule = raw_schedule.split(',')
            list_schedules.append(splitted_schedule)
    except:
        print('Error while converting raw schedules to listing')

    return list_schedules


# Function to read the data using all the other functions in the DAO file to return clean and operative data.
def read_data():
    raw_listing = load_employees_data()
    cleaned_listing = clean_employees_data(raw_listing)
    names, raw_schedules = split_data_in_name_and_schedule(cleaned_listing)
    schedules = raw_schedules_to_listing(raw_schedules)
    
    return names, schedules
