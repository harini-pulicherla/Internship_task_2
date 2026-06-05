vehicle_num=[1101,1102,1103,1104,1105,1106,1107]
tracking_id=[100000,100001,100002,100003,100004,100005,100006]
unique_id=[101,102,103,104,105,106,107]
delivery_status=["delivered","shipped","reached destination","not delivered","delivered","shipped","reached destination"]
def delivery_tracking():
       delivery_track=[]
       for i in range (len(vehicle_num)):
        tracking={"tracking_id":tracking_id[i],"unique_id":unique_id[i],"delivery_status":delivery_status[i],"vehicle_number":vehicle_num[i]}
        delivery_track.append(tracking)
       
       id=int(input("Enter the tracking ID : "))
       print("\n\t\tTRACKING DETAILS")
       print(f"{'TRACKING ID':<15} | {'UNIQUE ID':<15} | {'DELIVERY STATUS':<20} | {'VEHICLE NUMBER':<15}")
       print("-"*90)
       for tracking in delivery_track :
        if id==tracking['tracking_id']:
          print(f"{tracking['tracking_id']:<15} | {tracking['unique_id']:<15} | {tracking['delivery_status']:<20} | {tracking['vehicle_number']}")
       
       return delivery_track
