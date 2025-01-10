import kbc_questions as q
# We have 12 levels of KBC to win the final prize
questions = q.get_questions()
levels = [1000, 2000, 5000, 10000, 25000, 50000, 100000, 150000, 200000, 250000, 500000, 1000000]
money = 0

print("Welcome to KBC Kon Banega Crorepati!!!")

for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion for ${levels[i]} is")
    print(f"Q{i + 1}. {question[0]}")
    print(f"  a. {question[1]}          b. {question[2]}")
    print(f"  c. {question[3]}          d. {question[4]}")

    while True:
        try:
            choice = input("Enter your choice (a, b, c, d) or 0 to quit: ").lower()
            if(choice != 'a' and choice !='b' and choice !='c' and choice !='d' and choice != '0'):
                raise ValueError('Please choose an option from a, b, c and d or Zero to Quit')
            break
        except ValueError as e:
            print(e)
        
    if choice == '0':
        if i == 0:
            money = 0
        else: 
            if i <=3:
                money = levels[i - 1] * 0.6
                print(f'You gave up early! ${levels[i - 1] - money} penalty deducted.')
            elif i<=7:
                money = levels[i - 1] * 0.7
                print(f'You gave up early! ${levels[i - 1] - money} penalty deducted.')
            else:
                money = levels[i - 1] * 0.8
                print(f'You gave up early! ${levels[i - 1] - money} penalty deducted.')
        break
        
    if choice == question[-1]:

        print(f"You answered correctly! Great job! You've won ${levels[i]} so far.")

        if i == 2: # After every 3rd correct answer price money will be updated
            money = levels[i]
        elif i == 5:
            money = levels[i]
        elif i == 8:
            money = levels[i]
        elif i == 11:
            money = levels[i]
            
        if i == 2 or i == 5 or i == 8:
            print(f"Congratulations! You have passed a milestone, and you're guaranteed ${money}.")
        elif i == 11:
            print(f"Congratulations! You've reached the final milestone! you're guaranteed ${money}.")
    else:
        print(f"\nSorry, {choice} is incorrect option. The correct option was {question[-1]}")
        break

print(f"\n The amount of money you are taking home is ${money}")
