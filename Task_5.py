from Task_1 import *
from Task_2 import *
from Task_3 import *
from Task_4 import *

while True:

 print("1. To register new vehicle")
 print("2. To Assign Driver")
 print("3. To check the Trip Expenses")
 print("4. To Track Deliveries")
 print("5. TO Exit")
 
 choice = int(input("Please Enter Your Choice To Proceed : "))
 if choice==1:
  vehicle_registration(vehicle_num,register_num)

 elif choice==2:
  driver_assignment()

 elif choice==3:
  trip_expenses()

 elif choice==4:
  delivery_tracking()

 elif choice==5:
    print("Exiting the system......!")
    break
 else:
  print("Please enter a valid choice")

 