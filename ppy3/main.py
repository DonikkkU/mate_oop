#1
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * 3.14
    def perimeter(self):
        return 2 * self.radius * 3.14
My_Cirlce = Circle(8)
print(My_Cirlce.area())
print(My_Cirlce.perimeter())

#2

class Employee():
    def __init__(self):
        self.employee = {
            'Name': [],
            'Post': [],
            'Age': [],
            'Salary': []
        }
        print('1. Имя работника: 2. Должность: 3. Возраст: 4. Зарплата')

    def Add_Employee(self):
        choice = 1
        if choice == 1:
            n = (input('Имя работника:'))
            a = (input('Должность:'))
            b = int(input('Возраст:'))
            c = int(input('Зарплата:'))
            self.employee['Name'].append(n)
            self.employee['Post'].append(a)
            self.employee['Age'].append(b)
            self.employee['Salary'].append(c)

    def info_employee(self):
        print('Имя работника:', self.employee['Name'])
        print('Должность:', self.employee['Post'])
        print('Возраст:', self.employee['Age'])
        print('Зарплата:', self.employee['Salary'])


class Manager(Employee):
    def init(self):
        self.employee = {
            'Name': [],
            'Post': ['Manager'],
            'Age': [],
            'Salary': []
        }

    def Add_Employee(self):
        choice = 1
        if choice == 1:
            n = (input('Имя работника:'))
            b = int(input('Возраст:'))
            c = int(input('Зарплата:'))
            self.employee['Name'].append(n)
            self.employee['Age'].append(b)
            self.employee['Salary'].append(c * 1.1)

    def info_manager(self):
        print('Имя менеджера:', self.employee['Name'])
        print('Должность:', self.employee['Post'])
        print('Возраст:', self.employee['Age'])
        print('Зарплата:', self.employee['Salary'])


sam = Employee()
sam.Add_Employee()
sam.info_employee()

tom = Manager()
tom.Add_Employee()
tom.info_manager()
#3
class Bank_account:
    def __init__(self):
        print('1. просмотр баланса 2.внесение денег 3. снятие денег 4. отправка денег 0. Завершить оперпцию')
        int(input('Выберите операцию которую вы хотите сделать: '))
        self.balance = 0
    def deposit(self):
        amount = int(input("Введите сумму для депозита: "))
        self.balance += amount
        print("\n Внесенная сумма:", amount)
    def withdraw(self):
        int(input('Выберите операцию который вы хотите сделать:'))
        amount = int(input("Введите сумму вывода: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Вы сняли:", amount)
        else:
            print("\n Недостаточно средств: ")

    def check_balance(self):
        print('1. просмотр баланса 2.внесение денег 3. снятие денег 4. отправка денег 0. Завершить оперпцию')
        int(input('Выберите операцию который вы хотите сделать:'))
        print("\n Ваш баланс =", self.balance)
    def send_money(self):
        print('1. просмотр баланса 2.внесение денег 3. снятие денег 4. отправка денег 0. Завершить оперпцию')
        int(input('Выберите операцию который вы хотите сделать:'))
        int(input('Введите номер банкосвокой карты:'))
        amount = int(input('Введите колличетсво денег чтобы выслать:'))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Вы Отправили:", amount)
        else:
            print("\n Недостаточно средств: ")
        print("\n Ваш баланс =", self.balance)
    def stop(self):
        amount = int(input("Введите ноль чтобы завершить операцию:"))
        if amount == 0:
            print('Спасибо за выбор банкомата Академии!!!')








s = Bank_account()
s.deposit()
s.withdraw()
s.check_balance()
s.send_money()
s.stop()
