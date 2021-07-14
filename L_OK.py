class Employee():
    def __init__(self,workingDays,position,housingAllowance,familyAllowance):
        self.salary = 0
        self.workingDays = workingDays
        self.position = position
        self.housingAllowance = housingAllowance
        self.familyAllowance = familyAllowance

    # 給与計算処理
    def calculatePay(self):
        if self.workingDays > 0:
            self.salary += self.workingDays * 8000

class EmployeePositon(Employee):

    #役職による給与計算処理
    def calculatePay(self):
        super().calculatePay()

        if self.position == "課長":
            self.salary *= 1.2
        elif self.position == "部長":
            self.salary *= 1.5
        else:
            self.salary *= 1.0

class EmployeeHousingAllowance(Employee):

    #住宅手当による給与計算処理
    def calculatePay(self):
        super().calculatePay()

        if self.housingAllowance:
            self.salary += 3000

class EmployeeFamilyAllowance(Employee):
    
     #家族手当による給与計算処理
    def calculatePay(self):
        super().calculatePay()

        if self.familyAllowance:
            self.salary += 2000

if __name__=='__main__':
    tanaka = EmployeePositon(30,"課長",False,False)
    tanaka.calculatePay()
    print(tanaka.salary)

    yamada = EmployeeHousingAllowance(30,"平社員",True,False)
    yamada.calculatePay()
    print(yamada.salary)

    suzuki = EmployeeFamilyAllowance(30,"平社員",False,True)
    suzuki.calculatePay()
    print(suzuki.salary)