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

    
    
# text =123
# items ="abc"
# text ="Hi"
# items =None
text ="Python 3 is CALM."
print(clean_text(text))

