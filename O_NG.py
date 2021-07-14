class Employee():
    def __init__(self):
        self.salary = 0

    # 給与計算処理
    def calculatePay(self,workingDays,position,housingAllowance,familyAllowance):
        if workingDays > 0:
            self.salary += workingDays * 8000
        
        if position == "課長":
            self.salary *= 1.2
            return
        elif position == "部長":
            self.salary *= 1.5
            return
        else:
            self.salary *= 1.0

        if housingAllowance:
            self.salary += 3000
            return
        
        if familyAllowance:
            self.salary += 2000
            return

if __name__=='__main__':
    tanaka = Employee()
    tanaka.calculatePay(workingDays=30,position="課長",housingAllowance=False,familyAllowance=False)
    print(tanaka.salary)

    yamada = Employee()
    yamada.calculatePay(workingDays=30,position="平社員",housingAllowance=True,familyAllowance=False)
    print(yamada.salary)

    suzuki = Employee()
    suzuki.calculatePay(workingDays=30,position="平社員",housingAllowance=False,familyAllowance=True)
    print(suzuki.salary)
