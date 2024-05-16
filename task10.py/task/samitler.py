saitler = {'a', 'e', 'i', 'o', 'u'}

def samitleri_al(string):
    return {char for char in string 
            if char() and 
            char() not in saitler}