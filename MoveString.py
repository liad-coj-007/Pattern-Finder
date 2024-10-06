import string
class MoveString:
    """
    build MoveString
    object
    """
    def __init__(self,word) -> None:
        self.n = len(word)
        self.movemap = {word[i] : self.n - i - 1 
                        for i in range(self.n-1)}
    """
    get a char and return 
    its move string 
    """
    def __getitem__(self, ch):
        return self.movemap.get(ch, self.n)

    """
    overried operator print
    """
    def __str__(self):
        # This will be used for print()
        return f"Movemap is -> {self.movemap}"
    
