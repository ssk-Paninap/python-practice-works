angles = input("Input two angles of the triangle separated by comma: ")
ang_list = angles.split(',')
angle1 = int(ang_list[0])
angle2 = int(ang_list[1])
angle3 = 180 - angle1 - angle2

print(f"Third angle of the triangle: {angle3}")
