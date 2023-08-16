# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    first=int(input())
    third=str(input())
    second=int(input())
    fourth=str(input())
    x = third.split()[:first]
    a = set(x)
    y = fourth.split()[:second]
    b = a | set(y)
    
    print(len(b))
    