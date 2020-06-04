
def word_count(s):
    # Your code here
    counts = {}
    ignore = ['"',',',":",";",".","-","+","=","/","\\","|","[","]","{","}","(",")","*","^","&","\n","\t","\r","\r"]
    # split the word based on space
    word = s.split(" ")
    for c in word:
        c = c.lower()
        for i in ignore:
            if i in c:
                # strip the symbol in ignore from the words in c if they contain a symbol
                c = c.strip(i)
        # this will make it so spaces are not counted
        if len(c) == 0:
            continue       
        elif c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts
#search these and find what they do ----------------------------   
# makes trans
# translate
#-----------------------------------------------------------------       

# def print_letter_count(s):
#     counts = {}

#     for c in s:
#         #c = c.lower()  # case insensitive
#         if c in counts:
#             counts[c] += 1
#         else:
#             counts[c] = 1

#     items = list(counts.items())
#     items.sort(key=lambda e: e[1])
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count("Hello    hello"))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))