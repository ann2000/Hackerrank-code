import os
import sys

def equalStacks(h1, h2, h3):
    s1=sum(h1)
    s2=sum(h2)
    s3=sum(h3)
    while s1!=s2 or s1!=s3 or s2!=s3:
        m=max(s1,s2,s3)
        if m==s1:
            p=h1.pop(0)
            s1=s1-p
        if m==s2:
            p=h2.pop(0)
            s2-=p
        if m==s3:
            p=h3.pop(0)
            s3-=p
    return s1    


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
