def prime_number(num,list_num):
    sum=0
    for y in range(1,10000):
        if num%y==0:
            sum+=1
    if sum==2:
        return True
    else:
        return False
def add():
    return -2
def main():
    _list_ = []
    for i in range(1, 10000):
        true_false = prime_number(i,_list_)
        if true_false==True:
            _list_.append(i)
    print(_list_)
main()

