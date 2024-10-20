def word_count():
    with open(r'C:\Users\Pranav\Documents\Python Scripts\Python_Projects\random_50_word_text.txt','r')as file:
        words=file.read()
    mywords=words.split(" ")
    my_words={}
    for key in mywords :
        key=key.lower()
        if key not in my_words.keys():
            my_words[key]=1
        else:
            my_words[key]+=1
    return my_words
print(f"{'Key':<10} {'Value':<10}")
print('-' * 20)
for key,value in word_count().items():
    print(f"{key:<15}{value:<15}")

