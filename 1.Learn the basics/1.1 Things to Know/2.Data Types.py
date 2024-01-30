

# Finding the size of the give datatype
'''
    link: https://www.codingninjas.com/studio/problems/data-type_8357232
'''




def dataTypes(type: str):
    
    match type:
        case "Integer" | "Float":
            return 4
        case "Long" | "Double":
            return 8
        case "Character":
            return 1
    



data_type = input('Enter datatype')

print(dataTypes(data_type))