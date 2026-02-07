"""
    John Sebastian Laquis 
    Assignment #1
"""

gym_member = "Alex Alliton" # string
preferred_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # Boolean

workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (60, 15, 45),
    "Taylor": (20, 30, 30)
}

for friend in list(workout_stats.keys()):  # make a copy of the keys
    minutes = workout_stats[friend]
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes


# 2-dimensional list. A list of other lists
workout_list = [[friend, *minutes] for friend, minutes in workout_stats.items() if isinstance(minutes, tuple)]

print(f"{workout_list}")


for friend in workout_list:
    print(f"{friend[0]} - Yoga & Running: {friend[1:3]}")

for friend in workout_list[-2:]:
    print(f"{friend[0]} - Weightlifting: {friend[3]}")
    
for friend in workout_list:
    total_minutes = sum(friend[1:])  # sum of yoga, running, weightlifting
    if total_minutes >= 120:
        print(f"Great job staying active, {friend[0]}!")
        

name = input("Enter a friend's name: ").capitalize()

if name in workout_stats:
    yoga, running, weightlifting = workout_stats[name]
    total = workout_stats[f"{name}_Total"]

    print(f"{name}'s workout minutes:")
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {running} minutes")
    print(f"Weightlifting: {weightlifting} minutes")
    print(f"Total workout time: {total} minutes")
else:
    print(f"Friend {name} not found in the records.")
        
    
highest_friend = ""
lowest_friend = ""
highest_minutes = -1
lowest_minutes = float("inf")

for key, value in workout_stats.items():
    if "_Total" in key:
        friend_name = key.replace("_Total", "")

        if value > highest_minutes:
            highest_minutes = value
            highest_friend = friend_name

        if value < lowest_minutes:
            lowest_minutes = value
            lowest_friend = friend_name
print(f"Friend with the highest total workout minutes: {highest_friend}")
print(f"Friend with the lowest total workout minutes: {lowest_friend}")
