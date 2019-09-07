
m = open('Monster.txt')
monster = []
phase_in = []

for line in m:#open('Monster.txt'):
    line = line.rstrip()
    #print (line)
    monster.append(line)
#for word in m:
 #   print(word)
#print(len(monster))
#index = 0
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
for index in range (len(monster),0,-3): 
    for group_of_three in range (index,index-3,-1):
        phase_in.insert(0,monster[group_of_three-1])
    for line in range(0,len(phase_in)):
        print(phase_in[line])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    enter = input()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
    #index += 1
#print(monster[1])
'''
def hero_monster(file):
    unit = []
    phase_in = []
    for line in file:
        line = line.rstrip()
        #line = line.rjust(40)
        unit.append(line)
    for index in range (len(unit),0,3):
        for group_of_three in range(index,index-3,-1):
            phase_in.insert(0,unit[group_of_three-1])
        for line in range(0,len(phase_in)):
            print(phase_in[line])
        print()
        enter = input()
hero_monster(m)
for line in m:
    print(m)
'''          

'''
phase =  open('phase.txt','r')
phase_list = []
phase_animation = []
for line in open('phase.txt'):
    line = line.strip()
    phase_list.append(line)
    #print(line)
for time in range (1,1000):
    #print(time)
    for index in range (0,len(phase_list)):
        print(time)
        #print(len(phase_list))
        #print(index)
        phase_animation.append(phase_list[index])
        for line in range (0,len(phase_animation)):
            #print("line",len(phase_animation))
            print(phase_animation[line])
            print(phase_animation[line])
            print(phase_animation[line])
            print(phase_animation[line])
        enter = input()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        #print(45)
    #print(len(phase_animation))
    for index in range(len(phase_animation),0,-1):
        print(time)
        #print(2)
        phase_animation.remove(phase_animation[index-1])
        for line in range(0,len(phase_animation)):
            print(phase_animation[line])
            print(phase_animation[line])
            print(phase_animation[line])
            print(phase_animation[line])
        enter = input()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
'''        