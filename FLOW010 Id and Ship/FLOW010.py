# Go over the testCases
for testCases in range(int(input())):
    class_ID = input()
    if class_ID == "B" or class_ID == 'b':
        print("BattleShip")
    elif class_ID == "C" or class_ID == 'c':
        print("Cruiser")
    elif class_ID == "D" or class_ID == 'd':
        print("Destroyer")
    elif class_ID == "F" or class_ID == 'f':
        print("Frigate")
