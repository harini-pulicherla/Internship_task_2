vehicle_num=[1101,1102,1103,1104,1105,1106,1107]
distance=[258,351,420,395,330,444,495]
service_charge=[1200,1500,2000,3400,1600,1400,1655]
def trip_expenses():
       trip_expenses=[]
       fuel_cost=int(input("Enter the fuel cost per liter : "))
       for i in range (len(vehicle_num)):
        fuel_expense=fuel_cost*distance[i]     
        total_expense=fuel_expense+service_charge[i] 
        expenses={"vehicle_number":vehicle_num[i],"distance_travelled":distance[i],"service_charge":service_charge[i],"fuel_cost":fuel_expense,"total_trip_expense":total_expense}
        trip_expenses.append(expenses)
       
       print("\n=========================TRIP EXPENSES==================================")
       print("\n")
       print(f"{'Vehicle Number':<15} | {'Distance in KM':<15} | {'Service Charge':<15} | {'Fuel Cost':<15} | {'Total Trip Expense':20}")
       print("-"*90)
       for expenses in trip_expenses:
        print(f"{expenses['vehicle_number']:<15} | {expenses['distance_travelled']:<15} | {expenses['service_charge']:<15} | {expenses['fuel_cost']:<15} | {expenses['total_trip_expense']}")
       
       return trip_expenses


