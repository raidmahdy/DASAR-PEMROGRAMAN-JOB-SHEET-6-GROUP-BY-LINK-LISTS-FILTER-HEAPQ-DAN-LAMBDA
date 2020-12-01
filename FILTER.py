#List alfabet 
alfabet = ['a', 'b', 'c', 'e', 'i', 'k', 'o', 'z']
#fungsi penyaring huruf vocal 
def filter_vocal(alfabet): 
    vocal = ['a', 'i', 'u', 'e', 'o']
    if alfabet in vocal: 
        return True 
    else: 
        return False 
    
vocal_terfilter = filter(filter_vocal, alfabet)
print('Huruf vocal yang tersaring adalah:')
for vocal in vocal_terfilter:
    print (vocal)
