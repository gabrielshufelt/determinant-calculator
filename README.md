# determinant-calculator
Calculator program which allows user to find the determinant of a 2x2, or 3x3 matrix. Features a responsive and easy to use interface.
-----------------------
How to use it?
1. Select a matrix size.
2. Press "Select" button.
3. Enter ONLY INTEGER values (can be + or -) as entries
4. Press "Submit" button.
5. Determinant value will be shown in console.
-----------------------
This calculator makes use of simple additions and multiplications to calculate the determinant of
2x2 and 3x3 matrices. I made support for integer entries only but I did include code to recognize 
if the user enters something else than integer, and in that case it will tell the user that his
inputs are not valid (see code in matrix2.py for explanation). I used try and except method to counter
the ValueError that comes with trying to int(str).

