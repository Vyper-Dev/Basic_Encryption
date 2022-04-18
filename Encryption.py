run = True

#e x a m p l e
#_ _ _ _ _ _ _ _
#0 1 2 3 4 5 6 7
#No Special Chars or Capital Letters

while run == True:
    print("------------")
    print("1.Encrypt\n2.Decrypt")
    choice = input("")
    print("Enter your message:")
    
    def Encrypt():
        if ec[i] == 'a':
            ec[i] = '-'
        if ec[i] == 'b':
            ec[i] = '!'
        if ec[i] == 'c':
            ec[i] = '['
        if ec[i] == 'd':
            ec[i] = ':'
        if ec[i] == 'e':
            ec[i] = '3'
        if ec[i] == 'f':
            ec[i] = ';'
        if ec[i] == 'g':
            ec[i] = ')'
        if ec[i] == 'h':
            ec[i] = '$'
        if ec[i] == 'i':
            ec[i] = '8'
        if ec[i] == 'j':
            ec[i] = '&'
        if ec[i] == 'k':
            ec[i] = '@'
        if ec[i] == 'l':
            ec[i] = '"'
        if ec[i] == 'm':
            ec[i] = '}'
        if ec[i] == "n":
            ec[i] = '{'
        if ec[i] == 'o':
            ec[i] = '9'
        if ec[i] == 'p':
            ec[i] = '0'
        if ec[i] == 'q':
            ec[i] = '1'
        if ec[i] == 'r':
            ec[i] = '4'
        if ec[i] == 's':
            ec[i] = '/'
        if ec[i] == 't':
            ec[i] = '5'
        if ec[i] == 'u':
            ec[i] = '_'
        if ec[i] == 'v':
            ec[i] = '?'
        if ec[i] == 'w':
            ec[i] = '2'
        if ec[i] == 'x':
            ec[i] = ','
        if ec[i] == 'y':
            ec[i] = '7'
        if ec[i] == 'z':
            ec[i] = ']'
        if ec[i] == ' ':
            ec[i] = '|'
    
    def Decrypt():
        if dc[i] == '-':
            dc[i] = 'a'
        if dc[i] == '!':
            dc[i] = 'b'
        if dc[i] == '[':
            dc[i] = 'c'
        if dc[i] == ':':
            dc[i] = 'd'
        if dc[i] == '3':
            dc[i] = 'e'
        if dc[i] == ';':
            dc[i] = 'f'
        if dc[i] == ')':
            dc[i] = 'g'
        if dc[i] == '$':
            dc[i] = 'h'
        if dc[i] == '8':
            dc[i] = 'i'
        if dc[i] == '&':
            dc[i] = 'j'
        if dc[i] == '@':
            dc[i] = 'k'
        if dc[i] == '"':
            dc[i] = 'l'
        if dc[i] == '}':
            dc[i] = 'm'
        if dc[i] == '{':
            dc[i] = 'n'
        if dc[i] == '9':
            dc[i] = 'o'
        if dc[i] == '0':
            dc[i] = 'p'
        if dc[i] == '1':
            dc[i] = 'q'
        if dc[i] == '4':
            dc[i] = 'r'
        if dc[i] == '/':
            dc[i] = 's'
        if dc[i] == '5':
            dc[i] = 't'
        if dc[i] == '_':
            dc[i] = 'u'
        if dc[i] == '?':
            dc[i] = 'v'
        if dc[i] == '2':
            dc[i] = 'w'
        if dc[i] == ',':
            dc[i] = 'x'
        if dc[i] == '7':
            dc[i] = 'y'
        if dc[i] == ']':
            dc[i] = 'z'
        if dc[i] == '|':
            dc[i] = ' '
            
            
    if choice == "1":
        Run = True
        i = 0
        ec = list(input(""))
            
        while i < len(ec):
            Encrypt()
            i += 1
            if i == len(ec):
                print(*ec, sep='')
                break
    
    
    if choice == "2":
        Run = True
        i = 0
        dc = list(input(""))
        #print(dc)
        #print(dc[0])
        
        while i < len(dc):
            Decrypt()
            i += 1
            if i == len(dc):
                print(*dc, sep='')
                break
                
                
    if choice == "quit":
        break