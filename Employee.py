# Luke Matheson, ID: lcm95


class Employee:
    def __init__(self, employeeID, pay_rate):
        self.__employeeID = employeeID
        self.__hours = 0.0
        self.__pay_rate = float(pay_rate)
        self.__gross_wages = 0.0

    def __str__(self):
        return 'Employee ID: ' + self.__employeeID + '\n' + 'Hours: ' + str(self.__hours) + '\n' + 'Pay Rate: '  \
            + str(self.__pay_rate) + '\n' + 'Gross Wages: ' + str(self.__gross_wages)

    def getID(self):
        return self.__employeeID

    def getHours(self):
        return float(self.__hours)

    def setRate(self, new_rate):
        self.__pay_rate = new_rate

    def setHours(self, new_hours):
        self.__hours = float(new_hours)

    def setWages(self):
        self.__gross_wages = float(self.__hours) * float(self.__pay_rate)

    def getWages(self):
        return self.__gross_wages
