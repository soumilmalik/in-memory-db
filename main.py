import json 

def main():
    store={}
    
    while True: 
        line=input("Enter command: ").strip()
        if not line: 
            continue
        
        parts = line.split(maxsplit=2) #splits input into 3 parts , seperates first two wrods and keeps the rest as third part 
        command=parts[0].upper()

        if command=="SET":
            if len(parts)<3:
                print("wrong usage \n correct usage: SET <KEY> <VALUE>")
            else:
                key=parts[1]
                value=parts[2]
                store[key]=value
                print("done")

        elif command=="GET":
            if len(parts)<2:
                print("wrong usage \n correct usage: GET <KEY>")
            else:
                key=parts[1]
                if key in store:
                    print(store[key])
                else:
                    print("does not exist")

        elif command=="DEL":
            if len(parts)<2:
                print("wrong usage \n correct usage: DEL <KEY>")
            else:
                key=parts[1]
                if key in store:
                    del store[key]
                    print("done")
                else:
                    print("key already doesn't exist")

        elif command=="EXIST" or command=="EXISTS":
            if len(parts)<2:
                print("wrong usage \n correct usage: EXIST <KEY>")
            else:
                key=parts[1]
                if key in store:
                    print(True)
                else:
                    print(False)

        elif command=="SAVE":
            if len(parts)<2:
                print("wrong usage \n correct usage: SAVE <FILENAME>")
            else:
                filename=parts[1]
                with open(filename, "w") as f:
                    json.dump(store, f)
                    print("done")
        

        elif command=="LOAD":
            if len(parts)<2:
                print("wrong usage \n correct usage: LOAD <FILENAME>")
            else:
                filename=parts[1]
                try:
                    with open(filename, "r") as f: 
                        store=json.load(f)
                        print("done")
                except FileNotFoundError:
                    print("no such file found: ",filename)

        elif command=="QUIT":
            print("see you!")
            break

        elif command=="HELP":
            print(" SET KEY VALUE | GET KEY | DEL KEY | EXISTS KEY | SAVE FILE | LOAD FILE | QUIT")

        else:
            print("unknown command")

main()
