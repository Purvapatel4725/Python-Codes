def main():
    keywordsList = ["and","del","global","while","for","for","in","else","print","return","import","if","else","break","continue","elif","del","while","for","else"]
    dictionary = {} 
    count = 0
    for key in keywordsList:
        if key not in dictionary:
            dictionary[key] = 1
        else:
            count = dictionary[key]
            count+=1
            dictionary[key] = count
    sorted_dictionary = dict(sorted(dictionary.items(),key=lambda y:[1],reverse= True))
    print("Keyword_name   count")
    for key,value in sorted_dictionary.items():
        print(str(key).ljust(14),str(value))
            
    


main()
