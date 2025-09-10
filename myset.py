thisset = {"apple", "banana", "cherry"}
#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#Check if "banana" is not present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #If the item to remove does not exist, remove() will raise an error.
print(thisset)
#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)
#Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
print(x)
print(thisset)
#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)