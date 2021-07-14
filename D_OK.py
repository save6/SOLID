class Employee():
    def __init__(self,payCalculator):
        self.payCalculator = payCalculator

    # 給与計算処理
    def calculatePay(self):
        return self.payCalculator.calculatePay()

from abc import ABCMeta, abstractmethod
class PayCalculator(metaclass=ABCMeta):

     # 給与計算処理
    @abstractmethod
    def calculatePay(self):
        pass

class WorkingDaysPayCalculator(PayCalculator):
    def __init__(self,workingDays):
        self.workingDays = workingDays

    #役職による給与計算処理
    def calculatePay(self):
        salary = None

        if self.workingDays > 0:
            salary = self.workingDays * 8000
            
        return salary

class PositonPayCalculator(PayCalculator):
    def __init__(self,payCalculator,position):
        self.payCalculator = payCalculator
        self.position = position

    #役職による給与計算処理
    def calculatePay(self):
        salary = self.payCalculator.calculatePay()
        
        if self.position == "課長":
            salary *= 1.2
        elif self.position == "部長":
            salary *= 1.5
        else:
            salary *= 1.0
        
        return salary

class HousingAllowancePayCalculator(PayCalculator):
    def __init__(self,payCalculator,housingAllowance):
        self.payCalculator = payCalculator
        self.housingAllowance = housingAllowance

    #住宅手当による給与計算処理
    def calculatePay(self):
        salary = self.payCalculator.calculatePay()
        
        if self.housingAllowance:
            salary += 3000

        return salary

class FamilyAllowancePayCalculator(PayCalculator):
    def __init__(self,payCalculator,familyAllowance):
        self.payCalculator = payCalculator
        self.familyAllowance = familyAllowance

     #家族手当による給与計算処理
    def calculatePay(self):
        salary = self.payCalculator.calculatePay()
        
        if self.familyAllowance:
            salary += 2000

        return salary

if __name__=='__main__':
    tanaka = PositonPayCalculator(WorkingDaysPayCalculator(30),"課長")
    print(tanaka.calculatePay())

    yamada = HousingAllowancePayCalculator(WorkingDaysPayCalculator(30),True)
    print(yamada.calculatePay())

    suzuki = FamilyAllowancePayCalculator(WorkingDaysPayCalculator(30),True)
    print(suzuki.calculatePay())

    sudou = Employee(WorkingDaysPayCalculator(30))
    print(sudou.calculatePay())

    satou = FamilyAllowancePayCalculator(HousingAllowancePayCalculator(PositonPayCalculator(WorkingDaysPayCalculator(30),"課長"),True),True)
    print(satou.calculatePay())