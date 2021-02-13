from collections import Counter 
 
def no_dups(st): 
   st = st.split(" ")       
   for i in range(0, len(st)): 
      st[i] = "".join(st[i]) 
   dupli = Counter(st) 
   s = " ".join(dupli.keys()) 
   return s

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))