# 4.	Convert the given flowchart into Python code

def flowchart():
    print("Started: Travel from city A to B")
    time=input('Time : Longer or Shorter :-->').lower()
    if time == 'longer':
        price=input('Price : Lower or Higher : -->').lower()
        if price == 'lower':
            print('Coach')
            print('Arrived at city B')
        elif price =='higher':
            print('Train')
            print('Arrived at city B')
    if time == 'shorter':
        price=input('Price : Lower or Higher :--> ').lower()
        if price == 'lower':
            print('Red Eye Flight')
            print('Arrived at city B')
        elif price =='higher':
            print('Daytime Flight')
            print('Arrived at city B')
    

if __name__ == "__main__":
    flowchart()