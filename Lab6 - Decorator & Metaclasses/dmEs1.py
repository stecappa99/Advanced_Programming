import datetime


class Person:

    def __init__(self, name, lastname, birthday):
        self._name = name
        self._lastname = lastname
        self._birthday = birthday

    def getname(self):
        return self._name

    def getlastname(self):
        return self._lastname

    def getbirthday(self):
        return self._birthday

    def setname(self, value):
        self._name = value

    def setlastname(self, value):
        self._lastname = value

    def setbirthday(self, value):
        assert isinstance(value, datetime.datetime)
        self._birthday = value

    def __repr__(self):
        return "{0} {1} - Nato il {2}".format(self._name, self._lastname, self._birthday)


class Student(Person):

    def __init__(self, name, lastname, birthday, lectures):
        super().__init__(name, lastname, birthday)
        self._lectures = lectures

    def getgrade_average(self):
        return sum(self._lectures.values()) / len(self._lectures)

    def __repr__(self):
        return "{0} - Media dei voti: {1}".format(super().__repr__(), self.grade_average)

    grade_average = property(getgrade_average, None, None, "Media dei voti")


class Worker(Person):

    def __init__(self, name, lastname, birthday, pay_per_hour):
        super().__init__(name, lastname, birthday)
        self._pay_per_hour = pay_per_hour

    def getpay_per_hour(self):
        return self._pay_per_hour

    def setpay_per_hour(self, value):
        self._pay_per_hour = value

    salary_multiplier = lambda mult: property(lambda self: self.getpay_per_hour() * mult, lambda self, value:  self.setpay_per_hour(value / mult), None, "Proprietà")

    day_salary = salary_multiplier(8)
    week_salary = salary_multiplier(8 * 5)
    month_salary = salary_multiplier(8 * 5 * 4)
    year_salary = salary_multiplier(8 * 5 * 4 * 12)


class Wizard(Person):

    def get_age(self):
        return (datetime.datetime.today() - self.getbirthday()).days

    age = property(get_age, lambda self, value: self.setbirthday(value), None, "Eta")


if __name__ == "__main__":
    x = Wizard("Stefano", "Cappello", datetime.datetime(1999, 2, 10))
    print(x.age)
    x.age = datetime.datetime(2000, 1, 1)
    print(x.age)

