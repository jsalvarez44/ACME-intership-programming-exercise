__author__ = 'jsalvarez44'

# Class to define the Time object that has two integer parameters called hours & minutes.
class Time:
    # Constructor with parameters
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    # Function to compare two Time objects, return 0 if the times are equals, 1 if the current time is greater 
    # than the other time & return -1 if the current time is less than the other time.
    def compare(self, other):
        if self.hours == other.hours:
            if self.minutes == other.minutes: return 0
            elif self.minutes > other.minutes: return 1
            else: return -1
        elif self.hours > other.hours: return 1
        else: return -1


# Class to define the DateTime object that has a string parameter called day & two Time object parameters
# called entrance_time & departure_time.
class DateTime:
    # Constructor with parameters
    def __init__(self, day, entrance_time, departure_time):
        self.day = day
        self.entrance_time = entrance_time
        self.departure_time = departure_time


# Class to define the Employee object that has a string parameter called name & a list of DateTime 
# objects parameter called record.
class Employee:
    # Constructor with parameters
    def __init__(self, name, record):
        self.name = name
        self.record = record
        
