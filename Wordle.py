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
    """grey_indices=[]
    green_indices_ele=[]
    for i in range(5):
        if(pattern[i]==0):
            grey_indices.append(i)
        if(pattern[i]==2):
            green_indices_ele.append(word1[i])
    if(len(grey_indices)>0):
        for i in grey_indices:
            if word1[i] in green_indices_ele:
                continue
            if word1[i] in word2:
                return False
    return True"""
def yellow_check(word1,word2,yellow,green):
    """yellow_indices=[]
    green_indices=[]
    for i in range(5):
        if(pattern[i]==1):
            yellow_indices.append(i)
        if(pattern[i]==2):
            green_indices.append(i)
    not_green =[]
    for i in range(5):
        if i not in green_indices:
            not_green.append(i)
    c=0
    for x in yellow_indices:
        for j in not_green:
            if(x==j):
                continue
            if(word1[x] == word2[j]):
                c=c+1
                break
    return True if c==len(yellow_indices) else False"""
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
def play_wordle():
    words = get_words()
    wordle_word = get_random_word(words)
    print()
    print("Wordle word is "+wordle_word)
    print()
    pattern = [-1,-1,-1,-1,-1]
    final_pattern = [2,2,2,2,2]
    count=1
    while(True):
        print("#Guess "+str(count))
        print()
        type_word = input("Enter your Word:")
        if(wordle_word==type_word):
            print("\nYour Guess is Correct. Wordle Word is "+type_word)
            break
        pattern = compute_pattern(wordle_word,type_word)
        print("\nPattern : "+str(pattern))
        hashed_words = compute_hashed_words_with_same_pattern(pattern,type_word,words)
        print(hashed_words.count("niese"))
        words=hashed_words
        print("Recommended words for next time: ")
        try:
            for i in range(10):
                print(words[i])
        except:
            print()
        print()
        print()
        print()
        count=count+1
