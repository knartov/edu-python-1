# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        return '{} is moving'.format(self.name)

    def stop(self):
        return '{} is breaking'.format(self.name)

    def turn(self):
        return '{} is turning {}'.format(self.name, self.direction)


class SportCar:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        return '{} is moving'.format(self.name)

    def stop(self):
        return '{} is breaking'.format(self.name)

    def turn(self):
        return '{} is turning {}'.format(self.name, self.direction)


class WorkCar:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        return '{} is moving'.format(self.name)

    def stop(self):
        return '{} is breaking'.format(self.name)

    def turn(self):
        return '{} is turning {}'.format(self.name, self.direction)


class PoliceCar:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        return '{} is moving'.format(self.name)

    def stop(self):
        return '{} is breaking'.format(self.name)

    def turn(self):
        return '{} is turning {}'.format(self.name, self.direction)


if __name__ == '__main__':
    nissan = TownCar(140, 'red', 'almera', False, 'left')
    bmw = SportCar(250, 'black', 'Z4', False, 'right')
    gaz = WorkCar(120, 'white', 'gazel', False, 'left')
    ford = PoliceCar(200, 'blue', 'focus', True, 'right')
    print('{}, {}, {}, {}, {}'.format(nissan.name, nissan.direction, nissan.is_police, nissan.go(), nissan.turn()))
    print('{}, {}, {}, {}, {}'.format(bmw.name, bmw.direction, bmw.is_police, bmw.go(), bmw.turn()))
    print('{}, {}, {}, {}, {}'.format(gaz.name, gaz.direction, gaz.is_police, gaz.go(), gaz.turn()))
    print('{}, {}, {}, {}, {}'.format(nissan.name, nissan.direction, nissan.is_police, nissan.go(), nissan.turn()))


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, car_type):
        self.speed = speed
        self.color = color
        self.name = name
        self.car_type = car_type
        self.direction = direction

    def go(self):
        return '{} is moving'.format(self.name)

    def stop(self):
        return '{} is breaking'.format(self.name)

    def turn(self):
        return '{} is turning {}'.format(self.name, self.direction)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, weight):
        Car.__init__(self, speed, color, name)
        self.weight = weight


class SportCar(Car):
    def __init__(self, speed, color, name, upgrade):
        Car.__init__(self, speed, color, name)
        self.upgrade = upgrade


class TownCar(Car):
    def __init__(self, speed, color, name, places):
        Car.__init__(self, speed, color, name)
        self.places = places

