def windchill ():
    temp=int(input("Enter the temperature: "))
    velocity=int(input("Enter the velocity: "))

    windchill=35.74 + (0.6215 *temp) + ((0.4275*temp) - 35.75)*velocity**0.16

    print(windchill)

windchill()
