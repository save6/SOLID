class Employee():
    def __init__(self):
        self.salary = 0

    # 給与計算処理
    def calculatePay(self,workingDays):
        if workingDays > 0:
            self.salary += workingDays * 8000

class EmployeePositon(Employee):

    def __init__(self):
        super().__init__()

    #役職による給与計算処理
    def calculatePayByPosition(self,workingDays,position):
        super().calculatePay(workingDays)

        if position == "課長":
            self.salary *= 1.2
        elif position == "部長":
            self.salary *= 1.5
        else:
            self.salary *= 1.0

class EmployeeHousingAllowance(Employee):
    def __init__(self):
        super().__init__()

    #住宅手当による給与計算処理
    def calculatePayByHousingAllowance(self,workingDays,housingAllowance):
        super().calculatePay(workingDays)

        if housingAllowance:
            self.salary += 3000

class EmployeeFamilyAllowance(Employee):
    def __init__(self):
        super().__init__()

     #家族手当による給与計算処理
    def calculatePayByFamilyAllowance(self,workingDays,familyAllowance):
        super().calculatePay(workingDays)

        if familyAllowance:
            self.salary += 2000

if __name__=='__main__':
    tanaka = EmployeePositon()
    tanaka.calculatePayByPosition(30,"課長")
    print(tanaka.salary)

    yamada = EmployeeHousingAllowance()
    yamada.calculatePayByHousingAllowance(30,True)
    print(yamada.salary)

    suzuki = EmployeeFamilyAllowance()
    suzuki.calculatePayByFamilyAllowance(30,False)
    print(suzuki.salary)