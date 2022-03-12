# ACME programming exercise for an intership

## 1. Excercise statement

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

_Example 1:_

**INPUT**

  - RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
  - ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
  - ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


**OUTPUT:**

  - ASTRID-RENE: 2
  - ASTRID-ANDRES: 3
  - RENE-ANDRES: 2


_Example 2:_

**INPUT:**

  - RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
  - ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


**OUTPUT:**

  - RENE-ASTRID: 3
  
## 2. Solution

The input has a specific format, so it can be separated to store the data in different classes (following the object-oriented paradigm) and then process them to find the solution.

The algorithm of the solution consists of comparing each employee with the rest of their colleagues but without repetitions, comparing their schedule listings starting with the day and consequently, iterating and comparing their schedules to determine when they coincide at work on the same day at the same time. Finally, show on the screen the number of times that each employee has coincided at work with their colleagues.

## 3. Architecture

The architecture of the solution is based on the MVC (Model-View-Controller) & the DAO (Data Access Object) design patterns with a .txt file to consume the information.

![Architecture](https://user-images.githubusercontent.com/44406603/158012067-e85d080b-ecce-43a5-b5e2-862da2513a60.png)


## 4. Aproach

The approach that I found for the solution was to look at the patterns that the inputs had, then determine the cuts that I was going to make in the strings and finally design the classes that store these values.

## 5. Methodology

The methodology used in the development of the exercise was based on the object-oriented paradigm to use the MVC design pattern to structure the project and DAO to access the data located in the .txt file.
Once the general structure of the project was proposed, the DAO functions were developed to read, clean and organize the data to be able to process them from the controller. Then the models of all the classes (Time, DateTime, Employee) were developed and finally the view.
The solution algorithm is found in the controller and is based on dividing the input and cleaning it to be able to fill the classes correctly and then process it, each employee is compared with his colleagues but with the condition that there can be no repetitions. The days of attendance at work are compared and if they are the same, a comparison is made between the entrance time and the departure time following the three principal existing possibilities with three subposibilities each one for there to be a coincidence:

- If the first entrance time is equal to the second entrance time:
  - If the first departure time is equal to the second departure time:
    - We have a match!
  - If the first departure time is lower to the second departure time:
    - If the first entrance time is lower to teh second departure time:
      - We have a match!
  - If the first departure time is greater to the second departure time:
    - We have a match!
- If the first entrance time is lower to the second entrance time:
  - If the first departure time is equal to the second departure time:
    - We have a match!
  - If the first departure time is lower to the second departure time:
    - If the first entrance time is lower to teh second departure time:
      - We have a match!
  - If the first departure time is greater to the second departure time:
    - We have a match!
- If the first entrance time is greater to the second entrance time:
  - If the first departure time is equal to the second departure time:
    - If the second entrance time is lower to the first departure time:
      - We have a match!
  - If the first departure time is lower to the second departure time:
    - If the second entrance time is lower to the second departure time:
      - We have a match!
  - If the first departure time is greater to the second departure time:
    - If the second entrance time is lower to the first departure time:
      - We have a match!

If any of these conditions are met, we can conclude that there is a coincidence between two employees at work on the same day at the same time and in this way, we were increasing counter variables to know the expected result.

## 6. Instruction to run the project

### 6.1. Under any IDE that allows running python code:

 - Download the repository.
 - Open the extracted repository folder from the IDE of your choice.
 - Enter to the _project_ folder.
 - Run the _app.py_ file.

#### To run the unit tests:

 - Run the _test.py_ file.

### 6.2. In CMD or PowerShell:

 - Download the repository.
 - Open the extracted repository folder in a CMD or PowerShell.
 - Write ```cd project``` & Enter.
 - Write ```python app.py``` & Enter.

#### To run the unit tests:

 - Write ```python test.py``` & Enter.


## 7. Developed with 

* [Visual Studio Code](https://code.visualstudio.com/) - The IDE used
* [Python 3.7.8](https://www.python.org/downloads/release/python-378/) - The language used
* [unittest](https://docs.python.org/3/library/unittest.html) - The unit testing framework used






---



Developed with ❤️ by [Sebastian Alvarez](https://github.com/jsalvarez44)
