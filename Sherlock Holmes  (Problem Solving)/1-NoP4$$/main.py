# OUTPUT 477
import input
def is_valid_phrase(phrase):
    words = phrase.split()
    word_count = {}
    for word in words:
        if word in word_count:
            return False
        else:
            word_count[word] = 1
    return True

def count_valid_phrases(sentences):
    count = 0
    for sentence in sentences:
        if is_valid_phrase(sentence):
            count += 1
    return count

def main ():
    input_list = input.input_list
    print(count_valid_phrases(input_list))  
if __name__ == '__main__':
    main()