def prime_number(num,list):
    sum=0
    for y in range(1,10000):
        if num%y==0:
            sum+=1
    if sum==2:
        list.append(num)
        return list

def main():
    list = []
    for i in range(1, 10000):
        list = prime_number(i,list)
    print(list)
main()
