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
    
    return ans_list #list 

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

def text_report(text):
    """
    Generates a word statistics report from raw text.
    """
    if not isinstance(text,str):
        return {
            "total": 0,
            "unique": 0
        }

    cleaned_text = clean_text(text)
    result = word_stats(cleaned_text)

    return result

def number_stats(items):
    """
    Takes a list of items and returns numeric statistics.
    """

    # For non list inputs 
    if not isinstance(items, list):
        return {
                "total": 0,
                "positive": 0
            }
    
    total_count = 0
    positive_count=0

    for i in items:
        if isinstance(i,int):
            total_count+=1
            if i>0:
                positive_count+=1

    return {
            "total": total_count,
            "positive": positive_count
        }

# -------------------------------------------------------------
# Decision making starts ->>>
def basic_decision(text, items):
    """
    Makes a basic decision using text and number statistics.
    """
    cleaned_text = clean_text(text)
    text_stats = word_stats(cleaned_text)
    nums_stats = number_stats(items)

    if text_stats["total"]==0 and nums_stats["total"]==0:
        return "ignore"
    elif text_stats["total"]>=3 and nums_stats["positive"]>=1:
        return "accept"
    else:
        return "review"

def system_report(text, items):

    cleaned_text = clean_text(text)
    text_stats= word_stats(cleaned_text)
    nums_stats = number_stats(items)
    decision = basic_decision(text,items)

    return {
  "text": {
      "total_words": text_stats["total"],
      "unique_words": text_stats["unique"]
  },
  "numbers": {
      "total_numbers": nums_stats["total"],
      "positive_numbers": nums_stats["positive"]
  },
  "decision": decision
}

def decision_confidence(text, items):

    cleaned_text = clean_text(text)
    text_stats= word_stats(cleaned_text)
    nums_stats = number_stats(items)
    decision = basic_decision(text,items)

    if decision=="ignore":
        return 0
    elif decision=="review":
        return 50
    else:
        return 100

def confidence_label(score):
# Convert the numeric confidence into a human-readable label.(give the name to confidence)

    # For non int input 
    if not isinstance(score,int):
        return "unknown"
    
    if score==0:
        return "low"
    elif score==50:
        return "medium"
    elif score==100:
        return "high"
    else:
        return "unknown"

def confidence_report(text, items):

    score = decision_confidence(text,items)
    label = confidence_label(score)

    return {
            "score":score ,
            "label":label 
        }


text = "hello world"
items = [1]

print(confidence_report(text, items))



