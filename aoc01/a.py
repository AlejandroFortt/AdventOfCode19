accumulatedFuelForMass = 0

def extractFuel(fuel):
    return int(fuel/3) - 2

def totalFuelForMass(mass):
    global accumulatedFuelForMass
    accumulatedFuelForMass = 0
    while True:
        extraFuel = extractFuel(mass)
        if extraFuel > 0:
            mass = extraFuel
            accumulatedFuelForMass = accumulatedFuelForMass + extraFuel
        else:
            break
    return accumulatedFuelForMass

masses = [int(m) for m in open("input.txt").readlines()]

fuelForMasses = [totalFuelForMass(m) for m in masses]

totalFuel = sum(fuelForMasses)

print("El fuel requerido es:", totalFuel)
