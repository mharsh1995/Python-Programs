t=0
c=0
# Variables p and q and r in either true or false
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            # Regenerate input in simple way using Rules
            output=(p and q and not r) or ((p and not q) or r)
        # based on variables combinations we defind equation
        if output==True:
            t+=1
        else:
            c+=1
    # based on variables combinations we defind equation
    if t==8:
        print("Tautology")
    elif c==8:
        print("Contradiction")
    else:
        print("Contingency")