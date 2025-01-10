
import random
def get_questions():
    '''
    This module provides a list of general knowledge questions with multiple-choice answers.
    
    The `questions` list contains a set of questions, each represented by a list with the following structure:
        [question_text, option_a, option_b, option_c, option_d, correct_option]
    
    The correct option is represented by one of the letters: 'a', 'b', 'c', or 'd'.
    
    The module includes a feature to randomly select a subset of 12 questions from the original set of questions.
    '''
    questions = [
        ["What is the capital of Japan?", 'Beijing', 'Seoul','Tokyo', 'Kyoto', 'c'],
        ["Which country is known as the Land of the Rising Sun?", "China", "India", "Japan", "South Korea", 'c'],
        ["Who is the first man to walk on the Moon?", 'Neil Armstrong', 'Buzz Aldrin', 'Yuri Gagarin', 'Alan Shepard', 'a'],
        ["Where is Kabul?", "India", "Pakistan", "Iraq", "Afghanistan", 'd'],
        ["In which year did India gain independence from British rule?", 1942, 1947, 1950, 1965, 'b'],
        ["Who is the fastest man in the world?", "Andrew Tate", "Cristiano Ronaldo", "Usain Bolt", "Sachin Tendulkar", 'c'],
        ["How many strings does a guitar have?", 12, 18, 6, 10, 'c'],
        ["Which bone is the strongest in our body?", "Rib", "Femur", "Skull", "Back bone", 'b'],
        ["Which is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn", 'c'],
        ["In which year did the USA drop the nuclear bomb on Japan?", 2023, 1947, 1919, 1945, 'd'],
        ["What is the chemical formula of water?", "CO2", "H2O", "H2O2", "CH4", 'b'],
        ["Which is the smallest country in the world", "Bhutan", "Russia", "Vatican City", "Tokyo", 'c'],
        ['Which planet is known as the Red Planet?', 'Venus', "Mars", "Jupiter", "Saturn", 'b'],
        ['Which is the largest mammal in the world?', "Elephant", "Blue Whale", "Giraffe", "Whale Shark", 'b'],
        ['Who invented the telephone?', "Albert Einstein", "Alexandar Garaham Bell", "Nikola Tesla", "Thomas Edison", 'b'],
        ['Which of the following is the longest river in the world?', "Nile", "Amazon", "Ganga", "Yangtze", 'a'],
        ['What is the national flower of India?', 'Rose', "Jasmine", "Lotus", "Lilly", 'c'],
        ['Who is known as the "Father of the Nation" in India?', 'Jawaharlal Nehru', 'Sardar Vallabhbhai Patel', 'Mahatma Gandhi', 'Subhas Chandra Bose', 'c']
    ]
    return random.sample(questions,k= 12)

