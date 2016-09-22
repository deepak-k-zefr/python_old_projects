def union(p,q):
    for e in q:
         if e not in p:
             p.append(e)
    return p


p=[1,2,3]
q=[1,2,3,3,4,6,7]
print(union(p,q))
   
