class Dragon:
    def __init__(self, name):
        self.name = name
        self.health = 100


    def is_alive(self):
        return self.health > 0


    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0


    def talk(self):
        print(self.name, 'health', self.health, '. Hit My!')


    def final_cry(self):
        print(self.name, 'is dead...')


def main():
    enemy_list = [Dragon('Smog'), Dragon('Hidra'), Dragon('Archi')]
    finish = False
    while not finish:
        enemy = enemy_list[0]
        enemy.talk()
        damage = int(input('введите свой урон: '))
        if damage < 0:
            print('Здоровье восполнилось на ', abs(damage))
        if damage == 0:
            print('Здоровье не изменилось ')
        if damage > 0:
            print('Здоровье убавилось на ', abs(damage))
        enemy.get_damage(damage)
        if not enemy.is_alive():
            enemy.final_cry()
            enemy_list.pop(0)
        if not enemy_list:
            finish = True
    print('All the dragons are killed!')


main()

