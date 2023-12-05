class People:

    def earn_money(self):
        self.money += 1000
    def spend_money(self, amount):
        self.money -= amount
    def __str__(self):
        return f'Student{self.name}'

    def __init__(self, hungry, health, age, name, money, family, job, house, smart):
        self.hungry = 0
        self.health = 100
        self.name = name
        self.age = age
        self.money = money
        self.family = None
        self.job = None
        self.house = None
        self.smart = smart
    def buy_home(self, home):
        if home.price <= self.money:
            print('Congrats! You bought this house')
            self.house = home
            home.humans.append(self)
            self.money -= home.price
        else:
            print('Looks like you do not have enough money(')

    def buy_car(self, car):
        if car.price <= self.money:
            print('Congrats! Now you have new car!')
            self.car = car
            car.humans.append(self)
            self.money -= car.price
        else:
            print('Go and work(')
    def get_job(self):
        if self.smart >= 100:
            print('Hey! Now you have a job!')
        else:
            print('You are no soo good qualified(')
    def work(self):
        if  self.job is None:
            print('You have not job!')
        else:
            self.money += self.job.salary

class Home:
    def __init__(self,price):
        self.furniture = []
        self.humans = []
        self.price = price
    def __str__(self):
        return f'Home for{self.price}'
class Caffe(Home):
    def working(self):
        if len(self.humans) != 0:
            self.humans[0].money += 1000

class Car:
    def __init__(self,price):
        self.humans = []
        self.price = price
class rent_a_car(Car):
    def working(self):
        if len(self.humans) != 0:
            self.humans[0].money += 1000

class Job:
    def __init__(self,salary, name):
        self.salary = salary
        self.name = name
        self.timetable = None
stive = People('Stive', 20, 10000, 100)
job1 = Job(1000, 'police')
toyota1 = Car(15000)
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sleep = 0
    def do_sleep(self):
        self.sleep += 10
class Student(Human):
    def study(self):
        self.sleep -= 10
student = Student('Bob', 12)
student.do_sleep()
student.study()




