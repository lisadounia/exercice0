def cut_word(sentence):
        for i in range(len(sentence)):
            if (" " or ",") not in sentence:
                print(sentence)
                break
            else:
                 if sentence[i] == (" " or "," ) :
                     print(sentence[0:i])
                     sentence = sentence[i+1:]




print(cut_word("lisa dounia"))



