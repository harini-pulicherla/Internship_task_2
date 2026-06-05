
vehicle_num=[1101,1102,1103,1104,1105,1106,1107]
register_num=[11515,11516,11517,11518,11519,11520,11521]
seating_cap=[30,28,27,30,31,33,29]
def vehicle_registration(vehicle_num,register_num):
    vehicle_details=[]

    for i in range (len(vehicle_num)):
     
     vehicle={"vehicle_number":vehicle_num[i],"register_number":register_num[i],"seating_capacity":seating_cap[i]}
     vehicle_details.append(vehicle)

    print("------------------------Vehicle_Details-------------------------")
    print(f"{'Vehicle Number':<15} | {'Register Number':<15} | {'Seating Capacity':<15}")
    print("-"*60)
    for vehicle in vehicle_details:
     print(f"{vehicle['vehicle_number']:<15} | {vehicle['register_number']:<15} | {vehicle['seating_capacity']:<15}")
    return vehicle_details

