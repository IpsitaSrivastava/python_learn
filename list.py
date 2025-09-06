# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

if __name__ == '__main__':
    N = int(input())       # number of commands
    mylist = []            # start with empty list
    
    for _ in range(N):
        command = input().split()
        operation = command[0]
        
        if operation == "insert":
            i = int(command[1])
            e = int(command[2])
            mylist.insert(i, e)
            
        elif operation == "print":
            print(mylist)
            
        elif operation == "remove":
            e = int(command[1])
            mylist.remove(e)
            
        elif operation == "append":
            e = int(command[1])
            mylist.append(e)
            
        elif operation == "sort":
            mylist.sort()
            
        elif operation == "pop":
            mylist.pop()
            
        elif operation == "reverse":
            mylist.reverse()
