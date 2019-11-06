import time
from random import randint


def log(func):
    def wrapper(*args, **kwargs):
        my_arg = ''
        if func.__name__ == 'start_machine':
            my_arg = 'Start Machine\t'
        elif func.__name__ == 'boil_water':
            my_arg = 'Boil Water\t\t'
        elif func.__name__ == 'make_coffee':
            my_arg = 'Make Coffee\t\t'
        elif func.__name__ == 'add_water':
            my_arg = 'Add Water\t\t'
        user_log = '(bcarlier)Running:'
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        with open('machine.log', 'a+') as f:
            f.write(f'{user_log} {my_arg} [ exec-time =  {end_time - start_time:.3f} ms ]\n')
        return result
    return wrapper


class CoffeeMachine:
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
