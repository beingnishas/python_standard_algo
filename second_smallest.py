## Find second smallest number without using any inbuilt function
def second_smallest(x):
    sm1 = None
    p = x[0]
    for i in x:
        if sm1 is None or i < sm1:
            sm1 = i
    print("smallest number",sm1)
    
    # case 1: 5,9,2,3
    # case 2: 1,2,3,4
    for j in x:
        if j < p and j!=sm1 :
            p = j 
        # elif p == sm1 and j > sm1:
        #     p = j
    return p
    
print(second_smallest([100,50,64]))
print("s2",second_smallest([10,5,20,64,40,100]))


def sort_smallest(x):
    x.sort()
    return x[1]

print(sort_smallest([100,50,64]))
