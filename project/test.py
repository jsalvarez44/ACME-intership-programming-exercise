__author__ = 'jsalvarez44'

# import the unittest library to make unit tests & the libraries to test.
import unittest
from model.Model import Time
from model.DAO import clean_employees_data, split_data_in_name_and_schedule, raw_schedules_to_listing


# Class inherited from unittest.TestCase to define the test cases.
class ACMETesting(unittest.TestCase):

    # 1. Testing the Time.compare() method.

    # 01:00 < 02:00 -> expexted value: -1
    def test_time_compare1(self):
        first_time_object = Time(1, 0)
        second_time_object = Time(2, 0)

        COMPARATION = first_time_object.compare(second_time_object)
        EXPECTED_VALUE = -1

        self.assertEqual(COMPARATION, EXPECTED_VALUE)

    # 01:00 = 01:00 -> expexted value: 0
    def test_time_compare2(self):
        first_time_object = Time(1, 0)
        second_time_object = Time(1, 0)

        COMPARATION = first_time_object.compare(second_time_object)
        EXPECTED_VALUE = 0

        self.assertEqual(COMPARATION, EXPECTED_VALUE)

    # 02:00 > 01:00 -> expexted value: 1
    def test_time_compare3(self):
        first_time_object = Time(2, 0)
        second_time_object = Time(1, 0)

        COMPARATION = first_time_object.compare(second_time_object)
        EXPECTED_VALUE = 1

        self.assertEqual(COMPARATION, EXPECTED_VALUE)

    # 01:02 > 01:00 -> expexted value: 1
    def test_time_compare4(self):
        first_time_object = Time(1, 2)
        second_time_object = Time(1, 0)

        COMPARATION = first_time_object.compare(second_time_object)
        EXPECTED_VALUE = 1

        self.assertEqual(COMPARATION, EXPECTED_VALUE)

    # 01:02 < 01:03 -> expexted value: -1
    def test_time_compare5(self):
        first_time_object = Time(1, 2)
        second_time_object = Time(1, 3)

        COMPARATION = first_time_object.compare(second_time_object)
        EXPECTED_VALUE = -1

        self.assertEqual(COMPARATION, EXPECTED_VALUE)

    # 01:01 = 01:01 -> expexted value: 0
    def test_time_compare6(self):
        first_time_object = Time(1, 1)
        second_time_object = Time(1, 1)

        COMPARATION = first_time_object.compare(second_time_object)
        EXPECTED_VALUE = 0

        self.assertEqual(COMPARATION, EXPECTED_VALUE)

    # 2. Testing the DAO.clean_employees_data(raw_listing) method.

    # raw_listing: ['1234\n1234', '\n123\n123\n', '\nabc']
    # expected value: ['12341234', '123123', 'abc']
    def test_clean_employees_data(self):
        RAW_LISTING = ['1234\n1234', '\n123\n123\n', '\nabc']
        
        CLEANED_LISTING = clean_employees_data(RAW_LISTING)
        EXPECTED_VALUE = ['12341234', '123123', 'abc']
        
        self.assertEqual(CLEANED_LISTING, EXPECTED_VALUE)
    
    # 3. Testing the DAO.split_data_in_name_and_schedule(listing) method.
    
    # listing: [
        # 'JUAN=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00', 
        # 'ROSA=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
        # ]
    # expected_values: 
        # names: ['JUAN', 'ROSA']
        # schedules: [
            # 'MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00',
            # 'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
            # ]
    def test_split_data_in_name_and_schedule(self):
        LISTING = ['JUAN=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00', 'ROSA=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']
        
        NAMES, SCHEDULES = split_data_in_name_and_schedule(LISTING)
        EXPECTED_NAMES = ['JUAN', 'ROSA']
        EXPECTED_SCHEDULES = ['MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00','MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']
        
        self.assertEqual([NAMES, SCHEDULES], [EXPECTED_NAMES, EXPECTED_SCHEDULES])
    
    # 4. Testing the DAO.raw_schedules_to_listing(raw_schedules) method.
    
    # raw_schedules: [
        # 'MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00',
        # 'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
        # ]
    # expected_value: [
        # ['MO10:15-12:00', 'TU10:00-12:00', 'TH13:00-13:15', 'SA14:00-18:00', 'SU20:00-21:00'], 
        # ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']
        # ]
    def test_raw_schedules_to_listing(self):
        RAW_SCHEDULES = ['MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00','MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']
        
        LIST_SCHEDULES = raw_schedules_to_listing(RAW_SCHEDULES)
        EXPECTED_VALUE = [['MO10:15-12:00', 'TU10:00-12:00', 'TH13:00-13:15', 'SA14:00-18:00', 'SU20:00-21:00'], ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']]
    
        self.assertEqual(LIST_SCHEDULES, EXPECTED_VALUE)
    

if __name__ == '__main__':
    # Start the tests.
    unittest.main()
