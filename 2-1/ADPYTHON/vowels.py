def vowel(l):
    c='AEIOUaeiou'
    l1=list(c)
    for i in range(len(l)):
        if l1 in l:
            print("sentence contains all vowels")
            break
        else:
            print("does not contains all vowels")
            
n=input("enter asentence:")
l=list(n)
vowel(l)