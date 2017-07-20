print(list(map(__import__('functools').partial(lambda s,n:[s[i:i+n] for i in range(len(s)-n+1)],n=2),("I am an NLPer".split(),"I am an NLPer"))))

