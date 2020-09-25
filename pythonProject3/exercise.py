current_speed = int(input("enter current speed"))
average_speed_allowed = int(input("enter average speed"))
points = (current_speed - average_speed_allowed) // 5
if current_speed <= average_speed_allowed:
    print("OK")
elif current_speed > average_speed_allowed:
    print(points, "demerits")
    if points >= 12:
        print("time to go to jail")
else:
    print("incorrect entry")
