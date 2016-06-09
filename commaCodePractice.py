spam=['apples', 'bananas', 'tofu', 'cats']
yummyThings=['cheese', 'ice cream', 'mochi']

def comma(wordz):
    ughs=wordz[0:-1]
    for ugh in ughs:
        print (str(ugh) + ',', end='')
    print(' and ' + wordz[-1])
    


comma(spam)
comma(yummyThings)



