class SimpleHuman:

    def my_powers(self):
        print('I can walk and talk')


class Superman():

    def __init__(self, super_power):
        self.super_power = super_power

    def my_powers(self):
        print('I believe I can fly')
        self.super_power.my_powers()


class Ironman():

    def __init__(self, super_power):
        self.super_power = super_power

    def my_powers(self):
        print("I believe I'm the best. I'm ironman")
        self.super_power.my_powers()


if __name__ == "__main__":

    human = SimpleHuman()

    human = Superman(human)

    human = Ironman(human)

    human.my_powers()
