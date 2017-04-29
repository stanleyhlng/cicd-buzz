import unittest

from buzz import generator


def test_sample_single_word():
    population = (
        'foo',
        'bar',
        'foobar'
    )
    word = generator.sample(population)
    assert word in population


def test_sample_multiple_words():
    population = (
        'foo',
        'bar',
        'foobar'
    )
    words = generator.sample(population, 2)
    assert len(words) == 2
    assert words[0] in population
    assert words[1] in population
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
