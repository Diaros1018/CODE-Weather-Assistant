# Name: Diana Yanez
# CIS 3330
# CODE 1 - Weather Assistant
# Conversion formula: (Temperature in °F - 32) * .5556
# Note that the message to user should be the following
# "What is the temperature outside: "

def main():
    temperature_f = float(input("What is the temperature outside: "))

    temperature_c = (temperature_f - 32) * .5556

    if temperature_c > 20:
        print("\nWear a hat")
    elif temperature_c >= 10:
        print("\nWear a light jacket")
    else:
        print("\nWear a heavy jacket")


if __name__ == "__main__":
    main()
