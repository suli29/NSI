def combine_tableau(tab1 : list, tab2 : list):
    if len(tab1) == 0 and len(tab2) == 0:
        return[ ]
    elif len(tab1) == 0:
        return tab2
    elif len(tab2) == 0:
        return tab1
    else:
        if tab1[0] > tab2[0]:
            return [tab2[0]] + combine_tableau(tab1,tab2[1:])
        else:
            return [tab1[0]]

print(combine_tableau([2,3,5],[1,4]))
