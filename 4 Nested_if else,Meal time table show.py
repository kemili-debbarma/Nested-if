day=input("enter day")
meal_time=input("enter meal_time")
if day=="monday":
    if meal_time=="breakfast":
        print("poori sabji")
    elif meal_time=="lunch":
        print("sambhar rice")
    elif meal_time=="dinner":
        print("checken rice")
    else:
        print("no meal_time")
elif day=="tuesday":
    if meal_time=="breakfast":
        print("poha")
    elif meal_time=="lunch":
        print("rajma rice")
    elif meal_time=="dinner":
        print("roti sabji")
    else:
        print("non")
else:
    print("not day")