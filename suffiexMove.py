class suffiexMove():
    """
        build suffiex move 
        object
    """
    def __init__(self,word) -> None:
        self.n = len(word)
        self.lst = []
        for i in range(self.n):  
            self.lst.append(self.find_jump(word,i))
    
    """
    find letter jump of word
    """
    def find_jump(self,word,i):
        k = self.n - i - 1
        suffword = word[i+1:]
        findidx = self.last_occurrence_without_suffix(word, suffword, word[i])
        if findidx == None:
            return self.n + k
        
        return i - findidx + k
    
    """
    return the idx of the last letter
    without letter + suffiex
    on word
    """
    def last_occurrence_without_suffix(self,word, 
                                       suffix, letter):
        acc = self.find_all_suffix_occurrences(word,suffix)
        idx = None
        for i in acc:
            if word[i-1] != letter:
                idx = i - 1 
        return idx       

    """
    find all suffix occurenes
    on word
    """
    def find_all_suffix_occurrences(self,word, suffix):
        occurrences = [] 
        suffix_length = len(suffix)
        for i in range(-suffix_length,len(word) - suffix_length + 1):
            if word[max(i,0):i + suffix_length] in suffix:
                occurrences.append(i)  
        return occurrences
    

    """
    get val of the put on idx
    """
    def __getitem__(self, idx):
       if idx < 0 or idx >= len(self.lst):
          raise IndexError(f"{idx} out of range {len(self.lst)}")
       return self.lst[idx]
    
    """
    overried operator print
    """
    def __str__(self):
        # This will be used for print()
        return f"Suffiex is -> {self.lst}"


def main():
    str = "ABCXXX"
    suffiex = suffiexMove(str)
    print(suffiex)


if __name__ == "__main__":
    main()
