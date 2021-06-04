import _decimal
import importlib
import numbers
import string
import sys

def take_bill_amount(i) :
    print("Enter the Bill amount" +str(i+1)+ ":");
    bill=int(input());
    return bill;

def ask_for_type_of_share():
     type_of_share=input("you want share the expense/bill in percentage/exact amount\n");
     if type_of_share.lower()=="percentage":
                share_type = "percentage";
                return share_type;
     elif type_of_share.lower()=="amount":
        share_type = "amount";
        return share_type;         
     else:
        print("Please select any one of 2 options:");
        ask_for_type_of_share();
    


def   share_expense(no_people, bill, name, dshare, dict1, amount_owe):
    remain_per=100
    remain_bill=bill
    for n in range(no_people):
        type_of_share=input("you want share the expense/bill in percentage/exact amount\n");
        if type_of_share.lower()=="percentage" and n!=max(range(no_people)):
            share_type = "percentage";
            share_per=int(input("Enter % share for "+ name[n] +":should be equal or less than remaining percentage:\n"))
            amount_share=(share_per/100)*remain_bill;
            remain_per-=share_per
            remain_bill-=amount_share
            if(remain_per<0):
                print("given % share is invalid")
                sys.exit()
            print("remaining % of share:" + str(remain_per))
            print("amount to be given by "+ name[n] +" is:\n " + str(amount_share)+"\n")
            amount_owe[n]+=amount_share
            dict1={name[n]:amount_share}
            dshare.update(dict1)
        else:
            if n!=max(range(no_people)):
                share_per=int(input("Enter amount share for "+ name[n] +":should be equal or less than remaining amount to be shared:\n"))
            else:
                share_per=remain_bill
            remain_bill=remain_bill-share_per
            if(remain_bill<0):
                print("given amount share is invalid")
                sys.exit()
            print("remaining amount to be shared:" + str(remain_bill))
            print("amount to be given by "+ name[n] +" is:\n " + str(share_per)+"\n")
            amount_owe[n]+=share_per
            dict1={name[n]:share_per}
            dshare.update(dict1)
    print(dshare)
    print(amount_owe)
    return amount_owe



total=0
i=0
j=0
bill=list()
name=list()
dshare={}
dict1={}
print("Please Specify how many people including you:")
no_people = int(input())
amount_owe=[0] * no_people
for n in range (no_people):
    print("Enter name of people "+str(n+1)+":")
    fname=input()
    if fname not in name:
        name.append(fname)
        amount_owe[j]=0
        j+=1
while (True):
    if (i!=0):
             while(True):
                    prompt1=input("Do you still want to continue? Yes/No\n");
                    if prompt1.lower()=="yes":
                        break
                    elif ((prompt1.lower()) == "no"):
                        for k in range(no_people):
                            print("Total amount that has to be given by "+str(name[k])+" is:"+str(amount_owe[k]))
                        print("Total bill:"+ str(total))
                        sys.exit()
                    else:
                        continue
    bill.append(take_bill_amount(i))
    total+=bill[i]
    amount_owe=share_expense(no_people, bill[i], name, dshare, dict1, amount_owe)
    i=i+1