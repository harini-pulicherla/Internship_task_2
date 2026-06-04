from Task_1 import*
driver_name=["harish","tharun","chandu","ramu","ravi","chandra","sekhar"]
driver_number=[9133422126,7382860672,9492556119,7216484076,2763947673,5678926380,5764889890]
driver_ID=[1231,1232,1233,1234,1235,1236,1237]

def driver_assignment(driver_name,driver_ID,driver_number,vehicle_num):
       driver_details=[]
       for i in range (len(vehicle_num)):
        driver={"vehicle number":vehicle_num[i],"driver name":driver_name[i],"driver id":driver_ID[i],"driver number":driver_number[i]}
        driver_details.append(driver)

       print("\t \t DRIVER DETAILS") 
       print("-"*60)
       print(f"{'Vehicle Number':<15} | {'Driver Name':<15} | {'Driver ID':<15} | {'Driver Number':<15}")
       print("-"*60)
       for driver in  driver_details:
        print(f"{driver['vehicle number']:<15} | {driver['driver name']:<15} | {driver['driver id']:<15} | {driver['driver number']:<15}")
       return driver_details
       
driver_assignment(driver_name,driver_ID,driver_number,vehicle_num)

