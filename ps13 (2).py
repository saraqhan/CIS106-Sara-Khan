def dl1 (mylist):
  n = int(input("Number of items for your list: "))
  for n in range(0,n,1):
   s = int(input("Enter an integer: "))
   mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
    print(item)

mylist = []
mylist = dl1(mylist)
print(mylist)

mylist.insert(0,99)
print(mylist)

mylist[0] = 100
print(mylist)

mylist2 = ["Jones", "Adams", "Baker", "Smith"]
mylist3 = ["Rizzo", "Baez", "Bryant", "Baker"]
mylist2.extend(mylist3)
print(mylist)

mylist2.remove("Jones")
print(mylist2)

print("Count of Bakers in the list", mylist2.count ("Baker"))
print("Rizzo position in the list ",mylist2.index ("Rizzo"))