run = True

Characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
Key = ["-", "!", "[", ":", "3", ";", ")", "$", "8", "&", "@", '"', "}", "{", "9", "0", "1", "4", "/", "5", "_", "?", "2", ",", "7", "]", "|"]
#No Special Chars or Capital Letters

while run == True:
    Pos = 0
    print("------------")
    print("1.Encrypt\n2.Decrypt")
    choice = input("")
    print("Enter your message:")
            
    if choice == "1":
        Run = True
        Pos = 0
        ec = list(input(""))
            
        while Pos < len(ec):
            charpos = Characters.index(ec[Pos])
            ec[Pos] = Key[charpos]
            Pos += 1
        
        print(*ec, sep='')
    
    if choice == "2":
        Run = True
        Pos = 0
        dc = list(input(""))
        
        while Pos < len(dc):
            charpos = Key.index(dc[Pos])
            dc[Pos] = Characters[charpos]
            Pos += 1

        print(*dc, sep='')
                
    if choice == "quit":
        break