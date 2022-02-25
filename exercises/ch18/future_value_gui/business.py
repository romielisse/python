from dataclasses import dataclass

@dataclass
class Investment():
    monthlyInvestment:float = 0.0
    yearlyInterestRate:float = 0.0
    years:int = 0

    def calculateFutureValue(self):
        monthlyInterestRate = self.yearlyInterestRate / 12 / 100
        months = self.years * 12

        futureValue = 0
        for i in range(months):
            futureValue += self.monthlyInvestment
            monthlyInterestAmount = futureValue * monthlyInterestRate
            futureValue += monthlyInterestAmount

        return futureValue
