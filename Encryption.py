Characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
Key = ["-", "!", "[", ":", "3", ";", ")", "$", "8", "&", "@", '"', "}", "{", "9", "0", "1", "4", "/", "5", "_", "?", "2", ",", "7", "]", "|"]

while True:
    Pos = 0
    print("------------")
    print("1.Encrypt\n2.Decrypt")
    choice = input("Enter your choice: ")
    ec = list(input("Enter your message: "))
            
    if choice == "1":
        while Pos < len(ec):
            charpos = Characters.index(ec[Pos])
            ec[Pos] = Key[charpos]
            Pos += 1
    
    if choice == "2":
        while Pos < len(ec):
            charpos = Key.index(ec[Pos])
            ec[Pos] = Characters[charpos]
            Pos += 1
    print(*ec, sep='')