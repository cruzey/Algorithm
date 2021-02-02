from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다. ".format(name))

    def move(self, location):
        print("지상 유닛 이동")
        print("{} : {} 방향으로 이동합니다. [속도 {}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]"\
            .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다. ".format(self.name))
    
class Tank(AttackUnit):

    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.speed == 0
            self.seize_mode == True
        else:
            print("{} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.speed == 1
            self.seize_mode == False
            
         
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked == False
        else:
            print("{} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked == True
            
def game_start():
    print("게임이 시작되었습니다.")

def game_over():
    print("gg")

# 가상 게임 시작
game_start()

# 유닛 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

# 유닛 일괄 관리
unit_list = []
unit_list.append(m1)
unit_list.append(m2)
unit_list.append(m3)
unit_list.append(t1)
unit_list.append(t2)
unit_list.append(w1)

# 전군 이동
for unit in unit_list:
    unit.move("1시")

# 시즈모드 개발
Tank.seize_developed = True
print("시즈모드 개발 완료")

# 공격 준비
for unit in unit_list:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in unit_list:
    unit.attack("1시")

# 전군 피해
for unit in unit_list:
    unit.damaged(randint(5, 21))

game_over()

