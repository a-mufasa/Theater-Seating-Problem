# Movie Theater Seating Challenge
The goal is to implement an algorithm for assigning seats within a movie theater to fulfill reservation
requests. The arrangement of the theater has 10 rows with 20 seats per row. Our algorithm should maximize customer satisfaction and customer safety.

## Program Description
The entire program is written in Python and takes an input file via commandline and reads through the file
line by line to process each Reservation Request. There are 3 files:
1. Utility.py - processes the input file with functions for reading input and writing output
2. Theater.py - contains the MovieTheater class with methods for reserving/allocating seats according to the Algorithm and printing out a theater display and statistics.
3. Driver.py - contains the main() and calls to Utility.py and Theater.py to read the inputted file, allocate seats to the Request (print error messages for improper input), and write the output.txt file

## Assumptions
1. Our input text file will be in sequential order (R001, R002, R003, ...).
2. We cannot reserve seats for a request of larger size than the number of seats available.
3. For the sake of customer safety, customers must have 3 seats in between each other.
4. We will define the "best" seats as Row E, thus theater seats will fill up starting at the 1st columns of row E (close to center) and alternatively expand outwards.
 
## Algorithm
1. First come first serve allocation to the middle row (E).
2. Each group of reservations will be allocated to a single row if possible. If they are too large, we split
the group, and those that cannot fit into the row are placed in the next best row.
3. We repeat the process for as many requests as we can fit and if the theater cannot fit the next group, then
we tell them "insufficient seats" and try to fit any requests that meet the remaining seating.

## How to Run
1. Download the "Movie Theater Seating" folder.
2. Enter your terminal and set the path to the location of the folder (cd 'path').
3. Create your own input text files (.txt) or edit one of the existing test files following the input format "R### x" where R### is the reservation ID and x is the number of seats.
4. Type the following command with your choice of input file (make sure your system uses a version of Python 3.7 or newer):  
   ```python3 Driver.py input.txt```
6. A display of the seating will appear in the terminal after running and an output.txt file will be created containing the allocation of seats for each processed request. 

   If you want to test the program with a focus on Theater Utilization, you can decrease the *safety_buffer* value in Theater.py to 1.

## Discussion
Given more time, there are some changes I would've made to improve the project. Efficiency wasn't a priority
for this assignment but the project does well to make use of data structures, OOP, etc. so I with more time
for research and development, I would opt to use sparse matrices and/or graphs using a greedy algorithm where 
we assign weights to edges between an empty node and an occupied node. By minimizing the traversal, we can really
improve the speed of the program.

Another improvement I would've made with more time is a more well-rounded unit-testing method over multiple
input files. I would probably have a separate python file for inputting reservations and returning whether the test case has been passed/failed.

Having some form of User Interface would be handy but not necessary. It would also help with finishing the project as a fully dynamic movie theater seating algorithm (as shown by dynamic variable values).
