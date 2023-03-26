import prompt
import random



def main():
    print('Welcome to the Brain Games!')
    i = 0
    operator = ('+', '-', '*')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!\nWhat is the result of the expression?')
    while i < 3:
        oper = random.choice(operator)
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print(f'Question: {x} {oper} {y}')
        answer = prompt.string('Your answer: ')
        if oper == '+':
            expression = x + y
        elif oper == '-':
            expression = x -y
        else:
            expression = x * y
        if int(answer) == int(expression):
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {expression}.\nLet`s try again, {name}!')
            break
        i += 1
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()