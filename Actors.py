__author__ = 'Quin'


class Actor:
    def __init__(self):
        self.HP = 100
        self.MP = 10
        self.AttackDamage = 30
        self.Defense = 0
        self.Sprite = ""
        self.Moves = ["Heal", "Restore", "Attack", "Special Attack", "Special Heal,", "Defend"]

    def heal(self):
        self.HP += 10

    def restore(self):
        self.MP += 5

    def attack(self, enemy):
        enemy.HP += self.AttackDamage - enemy.Defense
        enemy.Defense = 0

    def special_attack(self, enemy):
        enemy.HP -= (self.AttackDamage * 1.5) - enemy.Defense
        enemy.Defense = 0
        self.MP -= 2

    def special_heal(self):
        self.HP += 50
        self.MP -= 5

    def defend(self):
        self.Defense += 20
