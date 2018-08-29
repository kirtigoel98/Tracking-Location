import csv
def main():
    flag=2
    with open("dataset.csv", "r+") as f:
        reader = csv.reader(f, delimiter=',')
        my_list = list(reader)
    file=open('dataset.csv','r+')
    str=file.read()
    if str is None:
        print ('FILE EMPTY\n')
    else:
        pin=input("ENTER PINCODE:\n" );
    if(len(pin)!=6):
        print ('INVALID PINCODE\n')
    else:
        for i in range(0,len(pin)):
            if(pin[i]<'0'or pin[i]>'9'):
                print ('INVALID PINCODE\n')
                break
    i=0
    for i in range(len(my_list)):
        if(pin==my_list[i][2]):
            print('LOCALITY:\t',my_list[i][0])
            print('POST OFFICE:\t',my_list[i][1])
            print('PINCODE:\t',my_list[i][2])
            print('SUB DISTRICT:\t',my_list[i][3])
            print('DISTRICT:\t',my_list[i][4])
            print('STATE:\t\t',my_list[i][5])
            print('\n')
            flag=True
    if(flag==False):
        print('PINCODE NOT FOUND\n')
