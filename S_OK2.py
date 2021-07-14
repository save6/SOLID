#共有データ
class Employee():
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

class PayCalculator():
    def __init__(self,employee):
        self.employeeData = employee

    # 給与計算処理
    def calculatePay(self):
        pass

class HourReporter():
    def __init__(self,employee):
        self.employeeData = employee

    # レポート出力処理
    def reportHours(self):
        pass

class EmployeeSaver():
    def __init__(self,employee):
        self.employeeData = employee

    # データベースへの保存処理
    def save(self):
        pass