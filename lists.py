fruits=["apple","banana","mango"]
print(fruits)
print(type(fruits))
print(len(fruits))

if "banana" in fruits:
    print("banana is part of list")
if "kiwi" not in fruits:
    print("kiwi isnot in the list")
    #indexing in list
    print(fruits[2])
    print(fruits[-1])
    print(fruits[0:2])

    fruits.append("kiwi")
    print(fruits)
    fruits.insert(2,"kiwi")
    print(fruits)
    morefruits=["guava","grapes"]
    fruits.extend(morefruits)
    print(fruits)

    fruits.remove("banana")
    print(fruits)
    fruits.pop(0)
    print(fruits)
    fruits.pop()
    print(fruits)

    #changing items in list

    fruits[1]="papaya"
    print(fruits)

   # fruits[1:3]= ["cherry"]
    #print(fruits)
    fruits.sort()
    fruits.sort(reverse=True)
    print(fruits)
    fruits.reverse()
    print(fruits)

    newfruits = [fruit for fruit in fruits if "a" in fruit]
    print(newfruits)

    newfruits=fruits.copy()
    newfruits=fruits+newfruits
    #nested list
    fruits.insert(2,["kiwi","papaya"])
    print(fruits)
    print(fruits[2][0])
    

