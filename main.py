import os
from file_read import  readfile, readjsonfile, writefile, writejsonfile;

import test_1;
import time;


def main():

    print("Starting program...")

    # test_1.printName("Snehal")

if __name__ == "__main__":

    try:

        main()
        # writefile()
        # readfile()
        # readjsonfile()
        writejsonfile()

        string = str(input())

        # print(string)
        while string != "exit":  
            string = str(input())

    except KeyboardInterrupt:

        print("CTRL_C Signal")

    finally:
                
        # print("Something...")
        os.system("pause")


        