# python-for-interviews
 Python Sytax for interviews 

---
##### Lambdas

![Lambda Syntax](./pictures/lambda.png 'lambda')

```python
   # Using map with lambda

   my_list=[1,2,3,4]
    
   # The first argument is the lambda , the second is the list
   
   my_list=list(map(lambda x:2*x,my_list))
   # you get the result as a map object type
   # You need to convert it back to a list before using it 
   
   print(my_list) # [2,4,6,8]

```

---
##### Recursion

The nth fibonacci number :

```python 

    def fib(n):
        if n<=1:
            return 0
        elif n==2:
            return 1
        else:
          return fib(n-1)+fib(n-2)
    
    if __name__ == "__main__":
    
        print(fib(6)) # Gives 5
     # Fib Numbers : 0 , 1, 1, 2, 3, 5
```
---
##### Loops

There are 2 loops in Python:
  1. **for loops**
  1. **while loops**

```python
 # Iterative fibonacchi 

    def fib(n):
        if n<1:
            return 0
        if n<=2:
            return 1
            
        count=2
        if n!=2:
            
        prev=0
        current=1
          n
        while count<n:
            # Swap prev and current , and the current
            # becomes prev+current 
            
           current,prev = current+prev,current
           count+=1
            
        return current 
        

```

##### A great way to the index of a character in a string is as follows.   
> This method successfully evades the danger of ValueError and    
> tells us the index , if character is present , else gives us `-1`
```python
def index_of(val, in_list,index):
    try:
        return in_list.index(val,index)
    except ValueError:
        return -1
```
---

### Data Structures   

#### Lists:

##### *Merging a List*  
> Python makes it really easy to merge lists together.   
> The simplest way is to use the + operator just like strings :
 
```python
     list1=[2,4]
     list2=[5,6]
     list3 = list1 + list2 # [2,4,5,6]
```

1. **Adding an element to a list**

    1. Adding an element to the end of the list
     
    ```python
      list=[1,2]
    
      list.append(4)
      
      list # [1,2,4]
    ```
    
    2. Inserting an element at a specific index
    
    ```python
    
    aList=[2,4,5]
    
    # Syntax For insertion : list.insert(index, newElement)
    
    aList.insert(1,3)
    
    aList # [2, 3, 4, 5] ( 3 is inserted at index 1 , 
    # If a value already exists at that index, the whole list
    # from that value onwards will be shifted one step to the right
    
    ```
   1. Removing elements from a list
   
       1. Removing from the end of the list :
   
            >    The counterpart of append() is the pop() operation    
            >    which removes the last element from the list.
            > 
            >    We can then `store` this `popped element` in a variable
            
            ```python
                   aList = [2, 4, 5]
                   popped = aList.pop()
                   print(popped) # 5
                    print(list) # [2,4]
            ```
          1. Removing the `first instance of an element` found from the list
               > If we need to delete a particular value from a list, 
               > we can use the remove() method by following this template :    
               `aList.remove(element_to_be_deleted)`
           
                ```python
                  aList = [2,4,5,5]
                  aList.remove(5)
                  
                  print(aList) # [2,4,5] , removed the first instance of 5
             
                  # For nested lists
                    populations = [["Winterfell", 10000], ["King's Landing", 50000],
                                   ["Iron Islands", 5000]]
                    print(populations)
                    populations.remove(["King's Landing", 50000])
                    print(populations) # [['Winterfell', 10000], ['Iron Islands', 5000]]
                ```
#### List Slicing