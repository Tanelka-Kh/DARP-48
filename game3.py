import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] 
    np.random.seed(1) 
    random_array = np.random.randint(1, 101, size=(1000)) 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) 

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)