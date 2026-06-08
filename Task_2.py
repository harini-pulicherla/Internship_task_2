from Task_1 import *

def driver_assignment():
       driver_details=[]
       for i in range (len(vehicle_num)):
        driver_name=input("Enter the driver name for vehicle {} : ".format(vehicle_num[i]))
        driver_ID=input("Enter the driver ID of {} : ".format(driver_name))
        driver_number=input("Enter the {} contact number :".format(driver_name))
        driver={"vehicle number":vehicle_num[i],"driver name":driver_name,"driver id":driver_ID,"driver number":driver_number}
        driver_details.append(driver)

       print("\n\t \t DRIVER DETAILS") 
       print("-"*60)
       print(f"{'Vehicle Number':<15} | {'Driver Name':<15} | {'Driver ID':<15} | {'Driver Number':<15}")
       print("-"*60)
       for driver in  driver_details:
        print(f"{driver['vehicle number']:<15} | {driver['driver name']:<15} | {driver['driver id']:<15} | {driver['driver number']:<15}")
       return driver_details
       

