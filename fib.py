import turtle



def crate_fib_list(n):
    fib_list = [1, 1]
    if n < 1:
        return fib_list
    if n == 1:
        return[1]
    if n == 2:
        return [1, 1]
    
    for i in range(n-2):
        last_num = fib_list[-1]
        second_last = fib_list[-2]
        fib_list.append(last_num+second_last)
    return fib_list


my_list = crate_fib_list(44)
print(my_list)
#for num in my_list:
   # print(num)
'''
mstr3sl = turtle.Turtle()

for num in my_list:
    mstr3sl.forward(num/10)
    mstr3sl.right(90)


mstr3sl.screen.mainloop()'''
print(my_list[-1]/my_list[-2])