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

    
# text =123
# items ="abc"
# text ="Hi"
# items =None
text ="Hello"
items =[1,2]
print(system_input(text, items))

