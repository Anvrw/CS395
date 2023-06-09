from view.view import View
from model.weather import Weather

class Controller:

    def __init__(self) -> None:
        self.view = View(self)
        self.weather = Weather()

        self.updateGUI()

    def main(self):
        self.view.main()

    def updateGUI(self):
        self.view.varLocation.set(self.weather.getLocation())
        self.view.varCondition.set(self.weather.getConditionText())
        self.view.varWindSpeed.set(self.weather.getWindSpeedMPH())
        self.view.varWindDir.set(self.weather.getWindDirection())

        if self.view.varUnits.get() == 1:
            self.view.varTemp.set(self.weather.getCurrentTempF())
            self.view.varFeelsLike.set(self.weather.getFeelsLikeF())
        else:
            self.view.varTemp.set(self.weather.getCurrentTempC())
            self.view.varFeelsLike.set(self.weather.getFeelsLikeC())

    def handleButtonSearch(self):
        location = self.view.varSearch.get()
        if location != '':
            self.weather = Weather(location)
            self.updateGUI()

    def handleComboLocation(self):
        pass