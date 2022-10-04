def main():
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i+12] #u
        if isPhoneNumber(chunk): #v
            print('Phone number found: ' + chunk)
    print('Done')

    
def isPhoneNumber(text):
    if len(text) != 12: #u
        return False
    
    for i in range(0, 3):
        if not text[i].isdecimal(): #v
            return False
        if text[3] != '-': #w
            return False

    for i in range(4, 7):
        if not text[i].isdecimal(): #x
            return False
        if text[7] != '-': #y
            return False
        
    for i in range(8, 12):
        if not text[i].isdecimal(): #z
            return False
        return True #{

if __name__ == '__main__':
    main()
