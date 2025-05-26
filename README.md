# 📘 Pattern-Finder
Efficiently find a word or phrase in a large `.txt` file and mark its occurrences.

## ⚙️ Usage
```bash
python3 StringFinder.py -w <word> -f <input_file> -o <output_file>
```
```
- word the word or phrase you want to find
- input_file the file to search in
- output_file - the file where the results will be written
on the output file every occurnce of the string will have on the start * 
that means the algorithm found it
```
# for example:
```
hello world. hello again.
```
and we search on this txt `hello` the output file will be
```
*hello world. *hello again.


