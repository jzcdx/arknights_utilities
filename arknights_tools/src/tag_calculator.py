"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
file = open("data_set2.txt", "r")

big_d = {}

#Processes files
def process(line):
    temp = line.split(":")
    
    c_tags = temp[0].split()
    
    #Removes the "-"'s from c_tags
    c_tags = list(filter(lambda a: a != "-", c_tags))
    
    c_ops = temp[1].strip()
    big_d[c_ops] = c_tags

    
line = file.readline()
if line != "":
    process(line)
while line != "":
    process(line)
    line = file.readline()
file.close()

print("-----------------------------------------------------------")
tags = input("Enter your tags separated by spaces: ").split()
matches = []
for i in big_d.items():
    key = i[0]
    vals = [x.lower() for x in i[1]]
    if set(vals) <= set(tags):
        matches.append(i)
print("-----------------------------------------------------------")
print("Matches: ")

if matches == []: 
    print("None")
else:
    for i in matches:
        print(i)


#print(set(t_c) <= set(tags)) #Checks if t_c is a subset of tags 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    