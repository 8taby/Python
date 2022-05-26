def get_word():
    answer_word = input('Input answer word: ')
    user_word = input('Input user word: ')
    return answer_word, user_word

def check_word(answer_word, user_word):
    green, yellow, gray = [], [], []
    for i in range(5):
		if user_word[i] not in answer_word:
			green.append(user_word[i])
		else:
			yellow.append(user_word[i])
		
    return green, yellow, gray

# ----------------------------------------------------------

answer_word, user_word = get_word()
green, yellow, gray = check_word(answer_word, user_word)

green.sort()
yellow.sort()
gray.sort()

print('Green: {0}'.format(green))
print('Yellow: {0}'.format(yellow))
print('Gray: {0}'.format(gray))