import random

class Gun:
    def __init__(self, gun_type):
        self.type = gun_type

class Animal:
    def __init__(self, animal_type):
        self.type = animal_type

class Game:
    def __init__(self):
        self.points = 0

    def start_game(self):
        print("Game started! Select a gun: 'pistol' or 'shotgun'")
        gun_type = input()
        gun = Gun(gun_type)
        animals = [Animal('rabbit'), Animal('deer'), Animal('bear')]
        while True:
            print("Shoot an animal ('q' to quit): ")
            animal_type = input()
            if animal_type == 'q':
                break
            animal = next((x for x in animals if x.type == animal_type), None)
            if animal:
                self.shoot(animal)
                animals.remove(animal)
            else:
                print("Invalid animal!")

    def shoot(self, animal):
        if animal.type == 'rabbit':
            self.points += 10
        elif animal.type == 'deer':
            self.points += 20
        elif animal.type == 'bear':
            self.points += 50
        print(f"Shot {animal.type}! Points: {self.points}")

    def end_game(self):
        print(f"Game ended! Total points: {self.points}")

game = Game()
game.start_game()
game.end_game()
