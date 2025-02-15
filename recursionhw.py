def other(o):
    if o == 1 :
        return 1
    else:
        return o+other(o-1)
print (other(999))