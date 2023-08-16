# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    first=int(input())
    third=str(input())
    second=int(input())
    fourth=str(input())
    b = set(third.split()[:first]) & set(fourth.split()[:second])
    print(len(b))
    