import math
from dataclasses import dataclass

@dataclass
class RightTriangle():
    sideA:int = 0
    sideB:int = 0

    @property
    def sideC(self):
        sumOfSquares = self.sideA ** 2 + self.sideB ** 2
        sideC = math.sqrt(sumOfSquares)        
        return sideC


def main():
    triangle = RightTriangle()
    print(triangle.sideC)

    triangle.sideA = 10
    triangle.sideB = 5
    print(triangle.sideC)
    

if __name__ == "__main__":
    main()
