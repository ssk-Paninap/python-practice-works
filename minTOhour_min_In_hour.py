hours = int(input("Input hours: "))
mins = int(input("Input minutes: "))
tot = (hours * 60) + mins

print(f"{hours} hours and {mins} mins is equal to : {tot} minutes")

mins = float (input("Input minutes : ")) 
hour  = mins/60
extra_min = mins % 60

print (f"{mins} has a total of {hour} and {extra_min} minutes")
