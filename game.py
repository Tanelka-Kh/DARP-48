# Импортируем библиотеку numpy 
import numpy as np
# Загадываем число от 1 до 100
# используем функцию RANDOM из библиотеки NumPy
number = np.random.randint(1, 101)
# Создаём переменную-счётчик для учёта количества попыток угадывания
count = 0
while True: 
    count += 1
    predict_number = int(input("Угадай число от 1 до 100:")) 
    
    if predict_number > number:
        print("Число должно быть меньше!")
    
    elif predict_number < number:
        print("Число должно быть больше!")
    
    else: 
        print(f"Вы угадали число! Это число {number}, за {count} попыток")
        break



