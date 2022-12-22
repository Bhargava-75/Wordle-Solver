import math
import numpy as np
def safe_log2(x):
    return -1*math.log2(x) if x > 0 else 0
def compute_entropies_allwords(WORD_FREQ_FILE):
    words_with_entropies=[]
    with open(WORD_FREQ_FILE) as fp:
        for line in fp.readlines():
            pieces = line.split(' ')
            word = pieces[0]
            freqs = [ float(piece.strip()) for piece in pieces[1:]]
            entropy = 0
            for freq in freqs:
                entropy = entropy + (freq*(safe_log2(freq)))
            words_with_entropies.append([word,round(entropy,5)])
    words = np.array([w[0] for w in words_with_entropies])
    entropies = np.array([w[1] for w in words_with_entropies])
    arg_sort = entropies.argsort()
    sorted_words = words[arg_sort]
    sorted_entropies = entropies[arg_sort]
    entropies_for_allwords = open("entropies_for_allwords_sorted.txt","w")
    for i in range(len(words)-1,-1,-1):
        entropies_for_allwords.write(sorted_words[i]+" "+str(sorted_entropies[i])+"\n")
    entropies_for_allwords.close()
WORD_FREQ_FILE = "all_words_freq.txt"
compute_entropies_allwords(WORD_FREQ_FILE)

            
