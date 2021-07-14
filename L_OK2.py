class Employee():
    def __init__(self,payCalculator):
        self.payCalculator = payCalculator

    # 給与計算処理
    def calculatePay(self):
        return self.payCalculator.calculatePay()

class PayCalculator():
    def __init__(self,workingDays,position,housingAllowance,familyAllowance):
        self.workingDays = workingDays
        self.position = position
        self.housingAllowance = housingAllowance
        self.familyAllowance = familyAllowance

     # 給与計算処理
    def calculatePay(self):
        if self.workingDays > 0:
            return self.workingDays * 8000

class PositonPayCalculator(PayCalculator):

    #役職による給与計算処理
    def calculatePay(self):
        salary = super().calculatePay()

        if self.position == "課長":
            salary *= 1.2
        elif self.position == "部長":
            salary *= 1.5
        else:
            salary *= 1.0
        
        return salary

class HousingAllowancePayCalculator(PayCalculator):

    #住宅手当による給与計算処理
    def calculatePay(self):
        salary = super().calculatePay()

        if self.housingAllowance:
            salary += 3000

        return salary

class FamilyAllowancePayCalculator(PayCalculator):
    
     #家族手当による給与計算処理
    def calculatePay(self):
        salary = super().calculatePay()

        if self.familyAllowance:
            salary += 2000

        return salary

if __name__=='__main__':
    tanaka = PositonPayCalculator(30,"課長",False,False)
    print(tanaka.calculatePay())

    yamada = HousingAllowancePayCalculator(30,"平社員",True,False)
    print(yamada.calculatePay())

    suzuki = FamilyAllowancePayCalculator(30,"平社員",False,True)
    print(suzuki.calculatePay())

    sudou = Employee(PayCalculator(30,"社長",True,True))
    print(sudou.calculatePay())