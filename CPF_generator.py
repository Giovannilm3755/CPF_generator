import random
for _ in range(10):
    cpf = ''
    for _ in range(11):
        random_cpf = random.randint(0, 9)
        cpf += str(random_cpf)
    print(f'The generated CPF is {cpf}')

    def cnt(range_):
        list_ = []
        index = 0
        for i in range_:
            count = i * int(cpf[index])
            list_.append(count)
            total_sum = sum(list_)
            index += 1
        total_sum = (total_sum * 10) % 11
        total_sum = 0 if total_sum > 9 else total_sum
        return total_sum

    sum1 = cnt(range_=range(10, 1, -1))
    sum2 = cnt(range_=range(11, 1, -1))
        
    generated_cpf = f'{cpf[0:9]}{sum1}{sum2}'
    if cpf == generated_cpf:
        print('Valid CPF')
        print(generated_cpf)
    else:
        print('Invalid CPF')
        print(generated_cpf)
