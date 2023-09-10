import subprocess

class DataStore:
    def __init__(self):
        self.integer = 0
        self.string = b'\x00' * 8

class Action:
    STORE_GET = 1
    STORE_SET = 2
    FLAG = 3

class Field:
    INTEGER = 1
    STRING = 2

def menu():
    res = {'act': 0, 'field': 0}
    print("\n(T)ry to turn it off\n(R)un\n(C)ry\n")
    choice = input(">> ").strip().upper()
    
    if choice == 'T':
        res['act'] = Action.STORE_SET
    elif choice == 'R':
        res['act'] = Action.STORE_GET
    elif choice == 'C':
        res['act'] = Action.FLAG
        return res
    else:
        print("\nWhat's this nonsense?!")
        exit(-1)

    print("\nThis does not seem to work.. (L)ie down or (S)cream\n")
    choice = input(">> ").strip().upper()
    
    if choice == 'L':
        res['field'] = Field.INTEGER
    elif choice == 'S':
        res['field'] = Field.STRING
    else:
        print("\nYou are doomed!\n")
        exit(-1)
    
    return res

def set_field(f):
    print("\nMaybe try a ritual?\n")
    data = input(">> ").strip()
    
    if f == Field.INTEGER:
        try:
            DataStore.integer = int(data)
            if DataStore.integer == 13371337:
                print("\nWhat's this nonsense?!")
                exit(-1)
        except ValueError:
            print("\nInvalid input for INTEGER.")
    elif f == Field.STRING:
        DataStore.string = data.encode('utf-8')

def get_field(f):
    print("\nAnything else to try?\n")
    
    if f == Field.INTEGER:
        print(DataStore.integer)
    elif f == Field.STRING:
        print(DataStore.string.decode('utf-8'))

def get_flag():
    if DataStore.integer == 13371337:
        subprocess.run(["cat", "flag.txt"])
        exit(0)
    else:
        print("\nSorry, this will not work!")

if __name__ == "__main__":
    DataStore = DataStore()
    print("\nSomething strange is coming out of the TV..\n")
    
    while True:
        result = menu()
        if result['act'] == Action.STORE_SET:
            set_field(result['field'])
        elif result['act'] == Action.STORE_GET:
            get_field(result['field'])
        elif result['act'] == Action.FLAG:
            get_flag()
