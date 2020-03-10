import numpy as np
count = 0
number = np.random.randint(1,100) 
def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
    
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
        Так-же проверяем больше оно, деленное на 2, или умноженное на 2, нужного.
        Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict:
            if number > (predict * 2):
                predict = predict * 2
            else:
                predict += 1
        elif number < predict:
            if (predict % 2) == 0:
                if number < (predict / 2):
                    predict = predict / 2
                else:
                    predict -= 1
            else:
                predict -= 1
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v2)