#!/usr/local/bin/python

'''
A python program to generate a random buzz.

'''
import random

BUZZ = (
    'continuous testing',
    'continuous integration',
    'continuous deployment',
    'continuous improvement',
    'devops'
)

ADJECTIVES = (
    'complete',
    'modern',
    'self-service',
    'integrated',
    'end-to-end'
)

ADVERBS = (
    'remarkably',
    'enormously',
    'substantially',
    'significantly',
    'seriously'
)

VERBS = (
    'accelerates',
    'improves',
    'enhances',
    'revamps',
    'boosts'
)


def sample(population, size=1):
    '''
    Sample population
    '''
    result = random.sample(population, size)
    if size == 1:
        return result[0]
    return result


def generate_buzz():
    '''
    Generate Buzz
    '''
    # print('generate_buzz()')
    buzz_terms = sample(BUZZ, 2)
    # print(buzz_terms)
    phrase = ' '.join([
        sample(ADJECTIVES),
        buzz_terms[0],
        sample(ADVERBS),
        sample(VERBS),
        buzz_terms[1]
    ])
    return phrase


if __name__ == '__main__':
    print(generate_buzz())
