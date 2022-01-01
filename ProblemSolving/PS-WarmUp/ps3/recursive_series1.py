'''
ps1 comprehension for problem
ps1.1. analysis
ps1.2. drawing pattern
pattern1.
factorial and bruteforce

pattern2.
factorial custom

ps2. applying computer algorithms to problem
ps2.1. utilizations

backtracking

ps2.2. integrations

ps3. Impl
'''

# control of recursive ; estimate success or not success => 1 or not 1, if not 1, then check promising not promising (0 or -1)
def ctrl_recursive(depth,limit,result):
    global samplespace, results
    
    promising=False
    if(depth<=1):
        promising=True
    else:
        if(all( x1+1==x2 for x1,x2 in zip(result[:depth-1],result[1:depth]))):
            promising=True

    if(depth>=limit):
        if(result[0]==1 and result[depth-2]+1==result[depth-1]):
            return 1
        else:
            return -1
    elif(depth<limit):
        if(promising):
            return 0
        else:
            return -1

# recursive for factorial, original version
def recursive_factorial(depth,limit,result):
    global samplespace, results
    # print('cur depth',depth,'result ',result, end=" => ")
    
    # backtracking part
    # token means 1,0,-1 which is success, not success(but promising), not success(and unpromising)
    token_ctrl=ctrl_recursive(depth,limit,result)
    # print('# token_ctrl ',token_ctrl)
    
    if(token_ctrl == 1):
        # print('success ',result)
        results.append(result)
    elif(token_ctrl == 0):
        for idx_fork,val_fork in enumerate(samplespace):
            result[depth]=val_fork
            recursive_factorial(depth+1,limit,result[:])
            result[depth]='*'
    else:
        pass

if __name__=="__main__":
    n=int(input())
    global samplespace
    samplespace=[item for item in range(1,11)]
    
    depth=0
    limit=n
    
    result=['*' for _ in range(n)]
    global results
    results=[]
    
    recursive_factorial(depth,limit,result)
    # print(results)
    
    if(n==1):
        print(1)
    
    for result in results:
        answer=1
        for item in result:
            answer*=item
        print(answer)