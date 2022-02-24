from dataclasses import dataclass

@dataclass
class Temp:
    __celsius:float = 0
    __fahrenheit:float = 32

    def getCelsius(self):
        return round(self.__celsius, 2)

    def setCelsius(self, celsius):
        self.__celsius = celsius
        self.__fahrenheit = celsius * 9/5 + 32

    def getFahrenheit(self):
        return round(self.__fahrenheit, 2)

    def setFahrenheit(self, fahrenheit):
        self.__celsius = (fahrenheit - 32) * 5/9
        self.__fahrenheit = fahrenheit


# the main function is used to test the Temp class
# this code isn't run if this module isn't the main module
def main():
    temp = Temp()
    for f in range(0, 212, 40):
        temp.setFahrenheit(f)
        print(temp.getFahrenheit(), "Fahrenheit equals", temp.getCelsius(), "Celsius")
    
    for c in range(0, 100, 20):
        temp.setCelsius(c)
        print(temp.getCelsius(), "Celsius equals", temp.getFahrenheit(), "Fahrenheit")

# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()

