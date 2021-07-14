class Employee():
    def __init__(self):
        self.salary = 0

    # 給与計算処理
    def calculatePay(self,workingDays):
        if workingDays > 0:
            self.salary += workingDays * 8000
        
    #役職による給与計算処理
    def calculatePayByPosition(self,workingDays,position):
        self.calculatePay(workingDays)

        if position == "課長":
            self.salary *= 1.2
        elif position == "部長":
            self.salary *= 1.5
        else:
            self.salary *= 1.0
    
    #住宅手当による給与計算処理
    def calculatePayByHousingAllowance(self,workingDays,housingAllowance):
        self.calculatePay(workingDays)

        if housingAllowance:
            self.salary += 3000

    #家族手当による給与計算処理
    def calculatePayByFamilyAllowance(self,workingDays,familyAllowance):
        self.calculatePay(workingDays)

        if familyAllowance:
            self.salary += 2000

if __name__=='__main__':
    tanaka = Employee()
    tanaka.calculatePayByPosition(30,"課長")
    print(tanaka.salary)

    yamada = Employee()
    yamada.calculatePayByHousingAllowance(30,True)
    print(yamada.salary)

    suzuki = Employee()
    suzuki.calculatePayByFamilyAllowance(30,False)
    print(suzuki.salary)