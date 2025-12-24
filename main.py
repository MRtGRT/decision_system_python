# Decision System Project
# Day 1: Project setup and planning

def system_input(text, items):
    """
    Takes raw inputs and returns a standardized dictionary.
    """
    # if not isinstance(text,str) and not isinstance(items,list):
    #     return {
    #             "text": "",
    #             "items": []
    #         }
    
  
    # Handling the bad input ->
    return {
            "text": "" if not isinstance(text,str) else text,
            "items": [] if not isinstance(items,list) else items
            }

def clean_text(text):
    """
    Takes a string and returns a list of lowercase words (letters only).
    """

    # For non string input
    if not isinstance(text,str):
        return []
    
    # converted into and splited on space
    words = text.lower().split()
    ans_list=[]

    for word in words:
        clean=""
        for i in word:
            if i.isalpha():
                clean+=i
        if clean=="":
            continue
        else:
            ans_list.append(clean)
    
    return ans_list

def word_stats(words):
    """
    Takes a list of words and returns basic statistics.
    """

    # Handling input other than list 
    if not isinstance(words, list):
        return {
            "total":0, 
            "unique": 0 
        }

    total_count=len(words)
    unique_count = len(set(words)) #more pythonic
    # freq={}

    # # For finding occurence of each word
    # for i in words:
    #     if i in freq:
    #         freq[i]+=1
    #     else:
    #         freq[i]=1

    # # For finding no. of unique elements
    # for i in freq.values():
    #     if i >=1:
    #         unique_count+=1
    
        
    return {
            "total": total_count, 
            "unique": unique_count 
        }

    


    
# words="hello"
words=["hello", "world", "hello"]
print(word_stats(words))

