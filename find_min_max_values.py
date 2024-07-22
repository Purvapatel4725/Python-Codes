'''As  a  member  of  the  Ontario  Tech  University  community,  I  share  our  community's commitment  to  the  highest  standards  of  academic  integrity  and  excellence  in  all dimensions of our work. 
I therefore promise that I will not lie, cheat, or use any unauthorized aids or assistance to complete any of my essays, assignments, and exams. 
I further promise that I will not offer any unauthorized assistance to any of my fellow students, and I promise that I will not ask any of my fellow students for unauthorized assistance. 
I promise that the work I submit is my  own  and  that  where  I  have  drawn  on  the  work  of  others,  I  have  included  proper attribution for my sources. 
Student name: Purva Patel 
student number: 100886734 '''


def findMinAndMax(values):
    min_value = values[0]
    max_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    return (min_value, max_value)

print(findMinAndMax([4,1,21,-7,9,13]))
print(findMinAndMax([-2,4,7,3,5,11,2,9])) 
print(findMinAndMax([7,10,4,30,-17,52]))