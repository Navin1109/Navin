l=['a','k','e','o','t','p','n']
w=['varun','arun','eat','peot','knife','net','toe','poe','vinus','ant','peacock','peak']
for i in w:
    i.lower()
    print(i)
    for j in i:
        print(j)
        print(j)
        if j not in l:
            w.remove(i)
            break
print(w)        
