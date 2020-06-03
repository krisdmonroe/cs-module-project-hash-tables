
def word_count(s):
    # Your code here
    counts = {}
    ignore = ['"',',',":",";",".","-","+","=","/","\\","|","[","]","{","}","(",")","*","^","&"]
    # split the word based on space
    word = s.split(" ")
    if len(s) == 0:
            return counts
    for c in word:
        c = c.lower()
        for i in ignore:
            if i in c:
                c = c.strip(i)
        if len(c) == 0:
            continue       
        elif c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts
        
       

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
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))