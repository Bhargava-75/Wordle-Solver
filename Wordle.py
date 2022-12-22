import random
def get_words():
    with open("entropies_for_allwords_sorted.txt") as fp:
        words=[ word.split(' ')[0] for word in fp.readlines()]
    return words
def get_random_word(words):
    wordle_word = random.choice(words)
    return wordle_word
def compute_pattern(wordle_word,type_word):
    pattern=[-1]*5
    matching = [False]*5
    for i in range(5):
        if(wordle_word[i]==type_word[i]):
            pattern[i]=2
            matching[i]=True
    rem_words1=[]
    rem_words2=[]
    for i in range(5):
        if(matching[i]!=True):
            rem_words1.append(wordle_word[i])
            rem_words2.append(type_word[i])
    rep=[]
    for i in range(5):
        if(matching[i]!=True):
            if type_word[i] not in rem_words1 or type_word[i] in rep :
                pattern[i]=0
                matching[i]=True
            else:
                rep.append(type_word[i])
    for i in range(5):
        if(matching[i]!=True):
            pattern[i]=1
    return pattern
def green_check(word1,word2,green): #word1 = typing word , word2 = all words
    for i in green:
        if(word1[i]!=word2[i]):
            return False
    return True
def grey_check(word1,word2,green,grey,yellow): #word1 = typing word , word2 = all words
    green_ele = [word1[i] for i in green]
    yellow_ele =[word1[i] for i in yellow]
    grey_ele = [word1[i] for i in grey]
    word2_without_green=""
    for i in range(5):
        if i not in green:
            word2_without_green=word2_without_green+word2[i]
    for i in grey_ele:
        if i not in green_ele and i not in yellow_ele:
            if i in word2:
                return False
        elif i in green_ele and i not in yellow_ele:
            if i in word2_without_green:
                return False
        elif i not in green_ele and i in yellow_ele:
            word1_count_i = yellow_ele.count(i)
            word2_count_i = word2.count(i)
            if(word2_count_i>word1_count_i):
                return False
        elif i in green_ele and i in yellow_ele:
            word1_count_i=yellow_ele.count(i)+green_ele.count(i)
            word2_count_i = word2.count(i)
            if(word2_count_i>word1_count_i):
                return False
    return True
def yellow_check(word1,word2,yellow,green):
    yellow_each_ele=[]
    for i in yellow:
        yellow_ind_ele=[]
        for j in range(5):
            if(i==j or j in green):
                continue
            else:
                yellow_ind_ele.append(word2[j])
        yellow_each_ele.append(yellow_ind_ele)
    for i in range(len(yellow)):
        if word1[yellow[i]] not in yellow_each_ele[i]:
            return False
    return True
            
def word_check(type_word,word,pattern,green,grey,yellow):
    if(green_check(type_word,word,green) and yellow_check(type_word,word,yellow,green) and grey_check(type_word,word,green,grey,yellow)):
        return True
    return False
def compute_hashed_words_with_same_pattern(pattern,type_word,words):
    hashed_words=[]
    green,grey,yellow=segregate_indices_in_pattern(pattern)
    for word in words:
        if(word==type_word):
            continue
        if(word_check(type_word,word,pattern,green,grey,yellow)):
            hashed_words.append(word)
    return hashed_words
def segregate_indices_in_pattern(pattern):
    green=[]
    grey=[]
    yellow=[]
    for i in range(5):
        if(pattern[i]==0):
            grey.append(i)
        elif(pattern[i]==1):
            yellow.append(i)
        elif(pattern[i]==2):
            green.append(i)
    return green,grey,yellow
