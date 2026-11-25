# Assignment No. 14 - Output
# Program: Logging with a divide function

"""
CONSOLE OUTPUT:

Dividing 10 by 2:
Result: 5.0

Dividing 10 by 0:
Result: None

Program execution completed!
Check app.log for execution details.


CONTENTS OF app.log:

2026-11-25 06:29:01,558 - INFO - Program started
2026-11-25 06:29:01,559 - INFO - Division function started
2026-11-25 06:29:01,559 - DEBUG - Values received: a=10, b=2
2026-11-25 06:29:01,559 - INFO - Division successful
2026-11-25 06:29:01,559 - DEBUG - Calculated result: 5.0
2026-11-25 06:29:01,559 - INFO - Division function started
2026-11-25 06:29:01,559 - DEBUG - Values received: a=10, b=0
2026-11-25 06:29:01,559 - ERROR - Cannot divide by zero
Traceback (most recent call last):
  File "ASSIGNMENT_14.py", line 31, in divide_numbers
    result = a / b
             ~~^~~
ZeroDivisionError: division by zero
2026-11-25 06:29:01,563 - INFO - Program finished

NOTE: Timestamps will differ on every run.
"""
