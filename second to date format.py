seconds = int(input("Enter the seconds : "))

hour = seconds // 3600
seconds = seconds % 3600

minute = seconds // 60
seconds = seconds % 60

print(f"{hour}:{minute}:{seconds}")
