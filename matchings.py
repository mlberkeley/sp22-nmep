import random
students = 'Annie, Verona, Atahan, Vedant, Ayushi, Shivansh, Diana, Ryan, Estella, Rishi, Evan, Mason, Jada, Inga'.split(', ')
print(students)
matchings = []
for i in range(len(students)//2):
    matchings.append([students.pop(random.randint(0, len(students)-1)), students.pop(random.randint(0, len(students)-1))])                                                        
print(matchings)

    
