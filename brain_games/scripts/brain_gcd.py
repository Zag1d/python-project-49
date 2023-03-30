import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    i = 0
    result = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nFind the greatest common divisor of given numbers.')
    while i < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        list_number = [num1, num2]
        list_number.sort(reverse=True)
        number1 = list_number[0]
        number2 = list_number[1]
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')
        if number1 % number2 == 0 and number2 % number1 == 0:
            result = number2
        elif (number1 % number2) % (number2 % (number1 % number2)) == 0:
            result = (number2 % (number1 % number2))
        else:
            remainder = []
            remainder.append(number1 % number2)
            remainder.append(number2 % number1)
            index = 0
            index2 = 1
            while (remainder[index] % remainder[index2]) != 0:
                if remainder[index2] == 0:
                    result = remainder[index2]
                    break
                remainder.append(remainder[index] % remainder[index2])
                result = remainder[-1]
                index += 1
                index2 += 1
            if int(answer) == result:
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer;(. Correct answer was '{result}'\nLwt`s try again, {name}!")
                break
            i += 1
        if i == 3:
               print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()