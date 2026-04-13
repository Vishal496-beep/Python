def even_generator(limit):
      for i in range(2,limit+1,2):
            yield i   

for num in even_generator(10):
        print(num)



# We are using yield instead of return because yield will stor value in memory and store it for so that the new loop or variable like 2 is stored so when we looped it yield first stored the value of i then it gave its value to num the stored one and then it generated even number

# yield memory m python k jis fnc m call hua h use rkhta h or sirf fnc hi nhi uski state ko bhi rkhta hai