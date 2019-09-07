import time
phase_list = []
phase_up = []
magic = []
space_ship = []
for line in open("phase.txt"):
    line = line.rstrip()
    phase_list.append(line)
for line in open("magic.txt"):
    line = line.rstrip()
    magic.append(line)
for line in open ("space_ship.txt"):
    line = line.rstrip()
    line = line[:len(line)-1]
    space_ship.append(line)
def phase_up_animation(phase_list,phase_up):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")      
    l = len(phase_list)
    for line in range(0,l):       
        time.sleep(.05)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
        phase_up.append(phase_list[0])
        phase_list.remove(phase_list[0])
        for line in phase_up:
            print(line)
    for line in open("phase.txt"):
        line = line.rstrip()
        phase_list.append(line)

def phase_down_animation(phase_list,phase_up):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")      
    l = len(phase_up)
    for line in range(0,l):       
        time.sleep(.05)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
        phase_list.insert(0,phase_up[len(phase_up)-1])
        phase_up.pop()
        for line in phase_up:
            print(line)
            
def phase_shift_animation(phase_up):
    l = len(phase_up)
    for shift_up in range(0,l-1):
        phase_up.append(phase_up[0])            
        phase_up.remove(phase_up[0])
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for line in phase_up:
            print(line)
        time.sleep(.05)


def phase_shift_down(phase_up):        
    l = len(phase_up)
    for shift_down in range(0,l-1):        
        phase_up.insert(0,phase_up[len(phase_up)-1])        
        phase_up.pop()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for line in phase_up:
            print(line)
        time.sleep(.05)
    return phase_up

def magic_animation(magic):
    new_magic = []
    for index in range(0,len(magic)-1):
        new_magic.append(magic[index])
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for line in new_magic:
            print(line)
        time.sleep(.05)
    l = len(new_magic)
    for line in range (0,l*1):
        time.sleep(.05)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        new_magic.append(new_magic[0])
        new_magic.remove(new_magic[0])
        for line in new_magic:
            print(line)
    return new_magic
    
def space_ship_in():
    cycle = 0
    for index in range(len(space_ship[cycle])-2,0,-1):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for line in range(0,len(space_ship)-4):
            print(space_ship[line][index:])
        print("\n\n\n\n")
        time.sleep(.04)
        cycle += 1
#space ship call
#space_ship_in()
#returns the index of the first char in string
def ship_index_finder(string):
    for index in range(0,len(string)):
        if string[index] != " ":
            #print("found it", index,string[index])
            return index +1
def light_index_finder(string,x):
    #find index of left most char    
        if x == 'right':        
            for index in range(len(string)-1,0,-1):
                if string[index] != " ":# or string[index] != " ":
                    #print("found it", index,string[index])
                    return index+1
    #find index of right most char    
        if x == 'left':
            for index in range(0,len(string)):
                if string[index] != " ":
                    return index
            #e=input()
                    
def ship_line_animation():
#sets string look    
    line3 = ".. . .."
    len3 = len(line3)
    line6 = "*O*O*"
    len6 = len(line6)+1
    line10 = "0~0"
    len10 = len(line10)
    line12 = ".~..~."
    len12 = len(line12)
    line14 = ".*.^.*."
    len12 = len(line12)
    msg = "OH NO!!! The martians are coming...                                      "
    msg2 = "Who will save use?                                                       "
#builds full string for each line    
    #line3
    for cycle in range (0,len(space_ship[2].strip())-2):
        line3 += " "
        line3 = " " + line3
    light_index3 = light_index_finder(line3,'right')
    ship_index3 = ship_index_finder(space_ship[2])
    #line 6
    for cycle in range(0,(len(space_ship[6].strip())-2)):
        line6 += " "
        line6 = " " + line6
    light_index6 = light_index_finder(line6,'left')
    ship_index6 = ship_index_finder(space_ship[6])
    #line 10
    for cycle in range(0,(len(space_ship[10].strip())-2)):
        line10 += " "
        line10 = " " + line10
    light_index10 = light_index_finder(line10,'right')
    ship_index10 = ship_index_finder(space_ship[10])
    #line 12
    for cycle in range(0,(len(space_ship[12].strip())-2)):
        line12 += " "
        line12 = " " + line12
    light_index12 = light_index_finder(line12,'left')
    ship_index12 = ship_index_finder(space_ship[12])
    #line14
    for cycle in range(0,(len(space_ship[14].strip())-2)):
        line14 += " "
        line14 = " " + line14
    light_index14 = light_index_finder(line14,'right')
    ship_index14 = ship_index_finder(space_ship[14])
    
    #sets counters
    line6_counter = 0
    line3_counter = 0
    line12_counter = 0
    line14_counter = 0
    bottom_counter = 4
    msg_counter = 0
    msg_counter2 = 0
#loops through full animation    
    for count in range (0,1):
        for count in range(0,2):
            for count10 in range(0,(len(space_ship[10].strip())-2)+len10):
        #line 10
                space_ship_line10 = (space_ship[10][:ship_index10]) + line10[light_index10-count10:len(line10)-count10] + "/"
        #line 3
                space_ship_line3 = (space_ship[2][:ship_index3]) + line3[light_index3-line3_counter:len(line3)-line3_counter] + "\ "
                line3_counter += 1
                if line3_counter > len(line3)/2-2:
                    line3_counter = 0
        #line 6 
                space_ship_line6 = (space_ship[6][:ship_index6]) + line6[0 + line6_counter:light_index6+line6_counter] + "("
                line6_counter += 1
                if line6_counter > len(line6)/2+2:
                    line6_counter = 0
        #line 12
                space_ship_line12 = (space_ship[12][:ship_index12]) + line12[0 + line12_counter:light_index12+line12_counter] + "/ "
                line12_counter += 1
                if line12_counter > len(line12)/2+3:
                    line12_counter = 0
        #line 14
                space_ship_line14 = (space_ship[14][:ship_index14]) + line14[light_index14-line14_counter:len(line14)-line14_counter] + "/"
                line14_counter += 1
                if line14_counter > len(line14)/2-2:
                    line14_counter = 0        
        #prints ship
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                for index in range(0,len(space_ship)):
                    if space_ship[index] == space_ship[2]:
                        print(space_ship_line3)
                    elif space_ship[index] == space_ship[6]:
                        print(space_ship_line6)
                    elif space_ship[index] == space_ship[10]:
                        print(space_ship_line10)
                    elif space_ship[index] == space_ship[12]:
                        print(space_ship_line12)
                    elif space_ship[index] == space_ship[14]:
                        print(space_ship_line14)

                    else:
                        print(space_ship[index])
        #display mgs
                if msg_counter != 1:
                    print(msg[:msg_counter2])
                    if msg_counter2 < len(msg):
                        msg_counter2 += 1
                    else: 
                        msg_counter2 =0
                        msg_counter +=1
                else:
                    print(msg2[:msg_counter2])
                    msg_counter2 += 1
                time.sleep(.06)

    
def animate_space_ship():
    counter = 0
    for line in space_ship:
        if line == space_ship[6]:
            ship_line_animation(counter)
            counter +=1
        else:
            print(line)
#animate_space_ship()
#ship_line_animation()    
#ship_index_finder(space_ship[6])    
'''
#brings phase up        
phase_up_animation(phase_list,phase_up)
#cycles throus phase shift

for count in range(0,2):
    phase_shift_animation(phase_up)
    phase_shift_down(phase_up)
#takes phase down
#phase_down_animation(phase_list,phase_up)
'''
'''
for line in phase_list:
    print(line)
'''
#magic_animation(magic)    