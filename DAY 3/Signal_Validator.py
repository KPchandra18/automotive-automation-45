def validateRange(value,minValue,maxValue):
    if value > maxValue:
        return 21
    elif value<minValue:
        return 31
    else:
        return 1




if __name__ == "__main__":
   
   msgs = ["BrakeFeature_FD", "Yaw_Data_FD","ACC_Data","ABS_Data"]
   
   msgData = {
       "BrakeFeature_FD": {
           "Veh_V_Brake": {"Value": 150,"minValue":0,"maxValue": 200},
           "Veh_Factor": {"Value": -1,"minValue":0,"maxValue": 1},
       },
   
       "Yaw_Data_FD": {
           "Veh_Yaw": {"Value": 8,"minValue":-6,"maxValue": 6},
           "Veh_Roll": {"Value": 0,"minValue":-6,"maxValue": 6},
       },
       "ACC_Data": {
           "ACCData_1": {"Value": 0,"minValue":-6,"maxValue": 6},
           "ACCData_2": {"Value": 0,"minValue":-6,"maxValue": 6},
       },
       "ABS_Data": {
           "ABSData_1": {"Value": 0,"minValue":-6,"maxValue": 6},
           "ABSData_2": {"Value": 0,"minValue":-6,"maxValue": 6},
       },
   
   }

   print("\nMessages in Database")
   print("    Message    |  Signal  |  Value  |  minValue  |  maxValue")
   for message in msgs:
   
       print("\n" + "-" * 30)
   
       for signal, value in msgData[message].items():
           def_val = value["Value"]
           minValue = value["minValue"]
           maxValue = value["maxValue"]
           print(f"{message}   {signal}   {def_val}   {minValue}   {maxValue}")
          
           
   
   system_running = 1
   
   
   while system_running == 1:
       totalMessages = 0
       totalSignal = 0
       testPassed = 0
       testFailed = 0
       for message in msgs:
           for signal, values in msgData[message].items():
               if validateRange(values["Value"],values["minValue"],values["maxValue"]) == 1:
                    print(f"{signal} data is within range and valid")
                    testPassed +=1
               elif validateRange(values["Value"],values["minValue"],values["maxValue"]) == 21:
                    print(f"{signal} data is invalid and exceeds max value")
                    testFailed +=1
               elif validateRange(values["Value"],values["minValue"],values["maxValue"]) == 31:
                    print(f"{signal} data is invalid and less than value")
                    testFailed +=1

               totalSignal+=1

           totalMessages+=1
        
       print(f"Total messages tested : {totalMessages} \nTotal signals tested  : {totalSignal}\nTotal tests passed    : {testPassed} \nTotal tests failed    : {testFailed}")
            
       
       system_running = int(input("System Running? (1/0) : "))