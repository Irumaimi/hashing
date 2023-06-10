import hashlib
class hash:
    def __init__(self):
        print("**********************************************************************")
        print("You can find in this program hash of the word & text                **")
        print("Also,you can find hash from the wordlist and you can add in the list**")
        print("**********************************************************************")
        print("Select you option form the choice: ")
        print("[1] Knowing the list of the hash algorithms in the program")
        print("[2] To Convert The text to hash as your algorithms select in the program")
        print("[3] To find the convert the to word if available in the wordlist")
        print("[4] To Add new word in the wordlist")
        print("[q] To exit the program")
        self.choice()
    def choice(self):
        try:
            while True:
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.list_of_hash()
                elif choice == '2':
                    self.convert_txt_hash()
                elif choice == '3':
                    self.find_hash()
                elif choice == '4':
                    self.add_to_wordlist()
                elif choice == "q" or choice == "Q":
                    break
                else:
                    print("you selected the wrong option. Please, select the correct option ..!")
        except Exception:
            print("There is wrong ...!")
    def list_of_hash(self):
        # shown the hash  algorithms in this lib
        print(hashlib.algorithms_guaranteed)

    def convert_txt_hash(self):
        text = str(input("Enter Your text to hash it: "))
        # select the type of hash and encode it
        hash_txt = hashlib.new(input("Enter the type of hash you want: "))
        print(hash_txt.hexdigest())
    def find_hash(self):
        try:
            while True:
                hashed_msg = str(input("Enter Your Hash : "))
                algorithms = input("Enter algorithm type : ")
                # open the file and read the contacts
                f = open("wordlist.txt", 'r')
                for line in f:
                    # split used to delete the space after the word , [0] to remove the list
                    text = line.split()[0]
                    encoded_txt = hashlib.new(algorithms, text.encode())
                    generated_hash = encoded_txt.hexdigest()
                    if generated_hash == hashed_msg:
                        print("[+] your msg is >>>>>>>> {}".format(text))
        except Exception:
            print("This hash not in our file ...")
        self.choice()
    def add_to_wordlist(self):
        # open the file and read the contacts
        file = open("wordlist.txt", 'a')
        file.write('\n' + str(input("Enter Your word to add in file: ")))
start_program = hash()