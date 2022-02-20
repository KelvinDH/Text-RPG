from time import sleep
import sys
from random import randint

class RPG:
    def __init__(self):
        self.healthpoints = 0
        self.manapoints = 0
        self.specialpoints = 0
        self.attack = 0
        self.defence = 0
        self.dexterity = 0
        self.Thunder = 0

    def getHealth(self):
            return self.healthpoints

    def getAttack(self):
            return self.attack

    def getThunder(self):
            return self.Thunder

    def setHealth(self, newHealth):
        self.health = newHealth

    def createPersonagem(self):
        self.name = str(input('Qual é o seu nome? '))
        self.classe = int(input('Qual classe você vai escolher?'
                                '[Guerreiro 1] '
                                '[Mago 2] '
                                '[Arqueiro 3] '))

        if self.classe == 1:
            self.classe = self.Guerreiro()
            print(f'Seja bem vindo {self.name}, você escolheu a classe: {self.classe[0]}')
            print('Carregando Status...')
            sleep(2.5)
            for pos in range(0, len(self.status_guerreiro)):
                print(f'{self.status_guerreiro[pos]::<1}', end=' ')

        elif self.classe == 2:
            self.classe = self.Mago()
            print(f'Seja bem vindo {self.name}, você escolheu o {self.classe[0]}')
            print('Carregando Status...')
            sleep(2.5)
            for pos in range(0, len(self.status_mago)):
                print(f'{self.status_mago[pos]::<1}', end=' ')

        elif self.classe == 3:
            self.classe = self.Arqueiro()
            print(f'Seja bem vindo {self.name}, você escolheu o {self.classe[0]}')
            print('Carregando Status...')
            sleep(2.5)
            for pos in range(0, len(self.status_arqueiro)):
                print(f'{self.status_arqueiro[pos]::<1}', end=' ')

    def Iniciar(self):
        self.TelaInicio()
        self.createPersonagem()
        self.Battle()

    def TelaInicio(self):
        while True:
            print('-=-' * 15)
            print('        Bem vindo ao RPG de Texto\n'
                  'Pressione "J" para jogar ou "S" para sair.')
            print('-=-' * 15)
            play = str(input('    >Jogar<\n'
                             '    >Sair<' )).strip().upper()
            if play == 'J':
                break
            else:
                quit()

    def Guerreiro(self):
        self.healthpoints = 220
        self.manapoints = 12
        self.specialpoints = 45
        self.attack = 21
        self.defence = 18
        self.dexterity = 15
        guerreiro = 'Guerreiro'
        self.status_guerreiro = ['HP:', self.healthpoints,
                                 'MP:', self.manapoints,
                                 'SP:', self.specialpoints,
                                 'ATK:', self.attack,
                                 'DEF:', self.defence,
                                 'DEX:', self.dexterity]

        return guerreiro, self.healthpoints, self.attack

    def Mago(self):
        self.healthpoints = 160
        self.manapoints = 50
        self.specialpoints = 12
        self.Mattack = 7
        self.defence = 16
        self.dexterity = 8
        self.Mthunder = 32
        mago = 'Mago'
        self.status_mago = ['HP:', self.healthpoints,
                            'MP:', self.manapoints,
                            'SP:', self.specialpoints,
                            'ATK:', self.Mattack,
                            'DEF:', self.defence,
                            'DEX:', self.dexterity]

        return mago, self.healthpoints, self.Mattack ,self.Mthunder

    def Arqueiro(self):
        self.healthpoints = 200
        self.manapoints = 8
        self.specialpoints = 55
        self.attack = 8
        self.defence = 18
        self.dexterity = 22
        arqueiro = 'Arqueiro'
        self.status_arqueiro = ['HP:', self.healthpoints,
                                'MP:', self.manapoints,
                                'SP:', self.specialpoints,
                                'ATK:', self.attack,
                                'DEF:', self.defence,
                                'DEX:', self.dexterity]

        return arqueiro, self.healthpoints, self.attack


    def Enemy(self):
        self.hp = 75
        self.Edefence = 10
        self.Eattack = randint(5, 8)
        self.enemy = 'Goblin'
        self.stats = ['HP', 75,
                      'DEF', 8]

        return self.enemy, self.Eattack, self.hp

    def getEHealth(self):
        return self.hp

    def getEAttack(self):
        return self.Eattack

    def setEHealth(self, newHealth):
        self.health = newHealth


    def Battle(self):
        print(f'\nO {self.Enemy()[0]} quer lutar!')
        while True:
            dados = randint(0, 20)
            choice = int(input(f'HP: {self.healthpoints} [Atacar - 1] [Magia - 2]'))
            if choice == 1:
                print('Rolando dado...')
                sleep(1.5)
                if dados > 5:
                    damage = self.classe[2]
                    self.hp = self.hp - damage
                    print(f'Você acertou o ataque! e causou {damage} de dano no inimigo')
                    print(self.hp)
                    if self.hp <= 0:
                        print(f'Você derrotou o {self.Enemy()[0]}')
                        break
                else:
                    print('Você errou o ataque...')
            if choice == 2:
                print('Rolando dado...')
                sleep(1.5)
                if dados > 5:
                    self.damage = self.classe[3]
                    self.hp = self.hp - self.damage
                    print(f'Você lançou uma magia no inimigo e causou {self.damage} de dano')
                    print(self.hp)
                    if self.hp <= 0:
                        print(f'Você derrotou o {self.Enemy()[0]}')
                        break
                else:
                    print('você errou o ataque')

                ''''hit = randint(0, 10)
                print(f'O {self.Enemy()[0]} se prepara pra um ataque...')
                sleep(1.5)
                if hit >= 3:
                    damageinimigo = self.Enemy()[1]
                    self.healthpoints = self.healthpoints - damageinimigo
                    print(f'Você perdeu {damageinimigo} pontos de HP')
                else:
                    print(f'O {self.Enemy()[0]} errou o ataque!')'''






rpg = RPG()
rpg.Iniciar()