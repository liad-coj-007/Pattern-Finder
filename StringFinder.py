import sys
from suffiexMove import suffiexMove
from MoveString import MoveString
import time


class StringFinder:
    """
    build string finder object
    """
    def __init__(self,word):
        self.word = word
        self.movemap = MoveString(word)
        self.suffiexmove = suffiexMove(word)

    """
    find on a str the word 
    return of list of idx where 
    the word is
    """
    def find(self,str):
        idx = self.movemap.n - 1
        lst = []
        while(idx < len(str)):
            j = self.movemap.n - 1
            i = idx
            while j >= 0:
                if str[i] == self.word[j]:
                    i -= 1
                    j -= 1
                else:
                    i = i + max(self.movemap[str[i]],
                                self.suffiexmove[j])
                    idx = i
                    break
            if j == -1:
                lst.append(i+1)
                idx += 1
        return lst

"""
return a list of all the idx
of word put on file that is dir
is path
"""
def find_str_on_file(word,path,outputpath):
    with open(path,"r") as infile:
        strfinder = StringFinder(word)
        txt = infile.read()
        start_time = time.time()  
        lst = strfinder.find(txt)
        write_with_operator(lst,txt,outputpath)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")  




"""
build args dictonary
if all the args exsit
"""
def flag_exists():
    flags = {'-w': 0, '-f': 0, '-o': 0}
    flag_keys = list(flags.keys())
    message = "Usage: python3 stringfinder.py -w <word> -f <file path> -o <output path>"
    args = {}
    arguments = sys.argv[1:]

    # Check for even number of arguments (flag + value)
    if len(arguments) % 2 == 1:
        print(f"{message}")
        exit(1)

    i = 0
    while i < len(arguments):
        if arguments[i] == '-w':
            flags['-w'] += 1
            # Capture word with spaces until the next flag
            word_parts = []
            i += 1
            while i < len(arguments) and arguments[i][0] != '-':
                word_parts.append(arguments[i])
                i += 1
            args["word"] = ' '.join(word_parts)  # Join the parts to form the complete word
            continue  # Skip incrementing i again
        
        elif arguments[i] == '-f':
            flags['-f'] += 1
            if i + 1 < len(arguments):
                args["file"] = arguments[i + 1]
                i += 2
            else:
                print(f"{message}")
                exit(1)

        elif arguments[i] == '-o':
            flags['-o'] += 1
            if i + 1 < len(arguments):
                args["output"] = arguments[i + 1]
                i += 2
            else:
                print(f"{message}")
                exit(1)
        
        else:
            print(f"{message}")
            exit(1)

    # Check that each flag is present exactly once
    if not all(flags[flag] == 1 for flag in flag_keys):
        print(f"{message}")
        exit(1)

    return args




def write_with_operator( idx, text, output_file):
    """
    Write the entire 'text' to a file, replacing the substrings at specified start indices 
    in 'idx' with those prefixed by an operator '*'.
    
    :param idx: A list of start indices where replacements should occur.
    :param text: The text from which to modify.
    :param output_file: The name of the output file to write to.
    """
  # Convert text to a list to facilitate modifications
    text_list = list(text)
    
    for index in sorted(idx, reverse=True):
        if 0 <= index < len(text):  
            text_list.insert(index, '*')

    modified_text = ''.join(text_list)

    with open(output_file, 'w') as file:
        file.write(modified_text)

def main():
    args = flag_exists()
    try:
        find_str_on_file(args["word"],args["file"],args["output"])
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    main()