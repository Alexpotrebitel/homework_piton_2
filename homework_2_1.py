# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2
n=int(input('Введите колличество монеток'))    
count_orel=0
count_reshka=0
min_kolichectvo=0
if 1<=n<=10:
    for i in range(1,n+1):
        temp=int(input("положение монетки 0 или 1 "))
        if temp>1 or temp<0:
            print('Неверное значение')
        if temp>0 and temp<2:
            count_orel+=1
        if temp==0:
            count_reshka+=1
    if count_orel>count_reshka:
        print(f'Нужно перевернуть {count_reshka} раз')
    else:
        print(f'Нужно перевернуть {count_orel} раз')
                
            # if i==n-1 and count>max_days:
            #   max_days=count  
#         else:  
#             if max_days<count:
#                 max_days=count
#             count=0
# print(max_days) 
      
            