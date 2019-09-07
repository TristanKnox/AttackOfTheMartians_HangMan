#Tristan Knox
#Game of Awsom
#12/4/2016

from Animation import phase_up_animation 
from Animation import phase_down_animation
from Animation import phase_shift_animation
from Animation import phase_shift_down
from Animation import magic_animation
import time
phase_list = []
#populats phase_list[]
for line in open("phase.txt"):
    line = line.rstrip()
    phase_list.append(line)
magic = []
#populats magic[]
for line in open("magic.txt"):
    line = line.rstrip()
    magic.append(line)
phase_up = []
phase_in_hero = []
phase_in_monster = []
mon2 = []
mon3 = []
#lower_monster = []




def import_unit(file):
    unit = []
    for line in file:
        line =  line.rstrip()
        unit.append(line)
    return unit

def phase_in_unit(unit,phase_in): 
    #if len(unit) != 0:
    for index in range(len(unit),0,-3):
        for group_of_three in range(index,index-3,-1):
            if len(unit) > 0:
                #print(unit[group_of_three-1])
                #print(len(phase_in))
                phase_in.insert(0,unit[group_of_three-1])
                unit.remove(unit[group_of_three-1])
        #print(len(unit))
        return phase_in

def phase_in_hero2(hero,phase_in_hero): 
    magic.append(magic_animation(magic))
    #phase_in_hero = phase_in_unit(hero,phase_in_hero)
    l = len(hero)
    ml = len(magic)
    for cycle in range(0,ml):
        if len(hero) > 0:
            phase_in_hero.insert(0,hero[len(hero)-1]) 
            hero.remove(hero[len(hero)-1])
        magic.remove(magic[len(magic)-1])
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for line in magic:
            print(line)
        for line in phase_in_hero:
            print(line)
        time.sleep(.1)
         
        #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        #for line in phase_in_hero: #phase_in_unit(hero,phase_in):
        #    print (line)
        #enter = input("Press Enter to continue:")
    return phase_in_hero
        
def phase_in_animation(monster,phase_in_monster):
    phase_up = []
    #brings phase up
    
    phase_up_animation(phase_list,phase_up)
    #e = input()
    #cycles throus phase shift
    for count in range(0,1):
        phase_shift_animation(phase_up)
        phase_shift_down(phase_up)
        #e = input()
    #phase_down_animation(phase_list,phase_up)
    return phase_up
  
  
  
def print_unit(unit):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for line in unit:
        print(line)
    enter = input("Press Enter to continue:")
    
def monster_parts(mon2,p_animation):
    mon2 = []
    l = len(p_animation)
    mon = phase_in_unit(monster,phase_in_monster)
    ml = len(mon)
    for index in range(len(mon)-1,-1,-1):
        mon3.insert(0,mon[index])
    mon = mon3
    for cycle in range(0,l):
        if len(mon) > 0:
            mon2.insert(0,mon[len(mon)-1])
            mon.remove(mon[len(mon)-1])
        else:
            p_animation.append("             ")
        p_animation.remove(p_animation[0])
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for line in p_animation:
            print(line)
        for line in mon2:
            print(line)
        time.sleep(.1)
    #print(len(mon3))
    #return mon3
def monster_animation():    
    #for cycle in range(1,8):
    p_animation = phase_in_animation(monster,phase_in_monster)
    monster_parts(mon2,p_animation)
    time.sleep(.1)

        
def phase_door_down(mon3):
    blank_list = []
    for count in range(1,20):
        blank_list.append("   ")
    print(len(blank_list))
    print(len(mon3))
    for line in mon3:
        print(line)
def hero():
    return
    
hero = import_unit(open("Hero.txt")) 
monster = import_unit(open("Monster.txt"))
'''
#Calls hero phase in
phase_in_hero2(hero,phase_in_hero)

#call Monster animation
for count in range(1,8):
	monster_animation()
	#e = input()
	#phase_door_down(mon3)
	#e =  input()
'''
'''
print(phase_in_monster)
e = input()
phase_in_monster2(monster,phase_in_monster)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
for line in phase_up:
    print(line)
#phase_in_monster2(monster,phase_in_monster)
#phase_in_monster2(monster,phase_in_monster)
#phase_in_monster2(monster,phase_in_monster)
#phase_in_monster2(monster,phase_in_monster)
#phase_in_monster2(monster,phase_in_monster)
#phase_in_monster2(monster,phase_in_monster)

'''


    
'''
#phase in monster while loop only needed for test
while len(monster) > 0:
    #print (len(monster))
    #e = input()
    if len(monster) == 0:
        break
    p = []
    p = phase_in_unit(monster,phase_in_monster)
    for line in p:
        print(line)
    #for line in phase_in_unit(monster,phase_in_monster):
    #    print(line)
    e = input()
'''
'''
print_unit(phase_in_monster2(monster,phase_in_monster))
for line in monster:
    print(line)
phase_in_monster = phase_in_unit(monster,phase_in_monster)
'''


#print_phased_unit(phase_in_monster)
'''
phase_in_hero = phase_in_hero2(hero,phase_in_hero)
for line in phase_in_hero:
    print(line)
enter = input()
'''

#phase_in_monster2(monster,phase_in_monster) 



'''
while len(hero) != 0:
    phase_in_hero = phase_in_unit(hero,phase_in_hero)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for line in phase_in_hero: #phase_in_unit(hero,phase_in):
        print (line)
    enter = input("Press Enter to continue:")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  
while len(monster) != 0:
    phase_in_monster = phase_in_unit(monster,phase_in_monster)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for line in phase_in_monster:
        print (line)
    enter = input("Press Enter to continue:")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

'''
 



