t=0
c=0
# Variables p and q in either true or false
for p in [True,False]:
    for q in [True,False]:
        # Regenerate input in simple way using Rules
        output=q and (not p or not q) and (p or not q)
        # if output is true hen add to check for tautology or contradiction or contingency
        if output==True:
            t+=1
        else:
            c+=1
    # based on variables combinations we defind equation
    if t==4:
        print("Tautology")
    elif c==4:
        print("Contradiction")
    else:
        print("Contingency")