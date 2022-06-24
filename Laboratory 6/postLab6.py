#post lab Laboratory 8
#1
from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width="1000", title="Temperature Converter")

        self.addLabel(text="Celsius", row=0, column=0)
        self.getInputCelsius = self.addFloatField(value=0.0, row=1, column=0)

        self.addLabel(text="Fahrenheit", row=0, column=1)
        self.getInputFahrenheit = self.addFloatField(value=32.0, row=1, column=1)

        self.btn1 = self.addButton(text=">>>>", row=2, column=0, command=self.computeFahrenheit)
        self.btn2 = self.addButton(text="<<<<", row=2, column=1, command=self.computeCelsius)

    def computeFahrenheit(self):
        val = self.getInputCelsius.getNumber()
        operation = 9.0 / 5.0 * val + 32
        self.getInputFahrenheit.setValue(operation)

    def computeCelsius(self):
        val = self.getInputFahrenheit.getNumber()
        operation = (val - 32) * 5.0 / 9.0
        self.getInputCelsius.setValue(operation)


def main():
    TemperatureConverter().mainloop()


if __name__ == "__main__":
    main()

