print()

degrees = float(input("Enter degrees: "))
decimal = degrees / 360
percent = decimal * 100
print(f"{degrees} degrees is {percent:.2f}% of a circle.\n")

percent = float(input("Enter a percent of a circle: "))
decimal = percent / 100
degrees = decimal * 360
print(f"{percent}% of a circle is {degrees:.2f} degrees.")
