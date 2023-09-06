#Formula: A = P * (1+r/t) ^ (nt)
#Where:
#A = amount after time t
#P = principal amount (your initial investment)
#r = annual interest rate (divide the number by 100)
#t = number of years
#n = number of times the interest is compounded per year

def CompInt(StartAmount: float, IntRate: float, Time: float, TimesPerYear: float):
    #print(StartAmount)
    #print(IntRate)
    #print(Time)
    #print(TimesPerYear)
    FracRate = IntRate / 100
    Interest = 1 + (FracRate/Time)
    FinalTotal = float(StartAmount * Interest)
    FinalTotal = FinalTotal ** TimesPerYear
    return FinalTotal


result = CompInt(100000, 5, 10, 2)
print(f"Final Total: {result}")