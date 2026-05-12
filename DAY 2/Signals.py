msgs = ["BrakeFeature_FD", "Yaw_Data_FD","ACC_Data","ABS_Data"]

msgData = {
    "BrakeFeature_FD": {
        "Veh_V_Brake": {"Value": 0,"MIn":0,"Max": 200},
        "Veh_Factor": {"Value": 1,"MIn":0,"Max": 1},
    },

    "Yaw_Data_FD": {
        "Veh_Yaw": {"Value": 0,"MIn":-6,"Max": 6},
        "Veh_Roll": {"Value": 0,"MIn":-6,"Max": 6},
    },
    "ACC_Data": {
        "ACCData_1": {"Value": 0,"MIn":-6,"Max": 6},
        "ACCData_2": {"Value": 0,"MIn":-6,"Max": 6},
    },
    "ABS_Data": {
        "ABSData_1": {"Value": 0,"MIn":-6,"Max": 6},
        "ABSData_2": {"Value": 0,"MIn":-6,"Max": 6},
    },

}

print("\nMessages in Database")
print("    Message    |  Signal  |  Value  |  Min  |  Max")
for message in msgs:

    print("\n" + "-" * 30)

    for signal, value in msgData[message].items():
        def_val = value["Value"]
        min = value["MIn"]
        max = value["Max"]
        print(f"{message}   {signal}   {def_val}   {min}   {max}")
       
        

system_running = 1

while system_running == 1:

    speed = int(input("\nEnter Vehicle Speed : "))

    msgData["BrakeFeature_FD"]["Veh_V_Brake"]["Value"] = speed

    if speed > 120:
        print("Over Speed Alert !!!!!")

    else:
        print("Running in Normal Speed")

    system_running = int(input("System Running? (1/0) : "))