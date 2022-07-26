from add_words import add_words_to_array


def test_add_unfiltered_word_to_array():
    array = []
    testWord = 'Hello!£$'
    expectedResult = 'Hello!£$'
    cut = add_words_to_array()
    result = cut.addWordsToArray(array, testWord)
    result = result[0]
    assert result == expectedResult


