def main():
    mass = int(input())
    new_value = energy(mass)
    print(new_value)


def energy(mass_value):
    energy_value = mass_value * 300000000**2
    return energy_value


main()