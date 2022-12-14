# Functions that helps in scrapping
# Remove Character from the text
def Remove_Character(Text, characters):
    if Text == None:
        return ''
    else:
        val = Text.get_text(separator=' ').rstrip().split()
        val = ' '.join(val)
        for c in characters:
            val = ''.join(val.split(c))
        return val
# Get the position value
def Get_Position_Value(Text_Value, value_address):
    if Text_Value == None:
        return ''
    else:
        val = Text_Value.get_text(separator=' ').rstrip().split()
        if len(val) == 0 :
            return "Null"
        elif len(val) <=  value_address:
            return "Null"
        else:
            return val[value_address]

# Join the array with given tag
def Join_Value_With(value, join_value):
    if value == None:
        return ''
    else:
        val = value.get_text(separator=' ').rstrip().split()
        val = join_value.join(val)
        return val

# To Reamove Unusal Spaces
def Remove_Unusal_Spaces(value):
    if value == None:
        return ''
    else:
        val = value.get_text(separator=' ').rstrip().split()
        val = ' '.join(val)
        return val

# Make the attributes naming
def Name_Attribute(attribute):
    if attribute == None:
        return ''
    else:
        # remove the unusual spaces and convert the sentence into array
        attr = attribute.get_text(separator=' ').rstrip().split()
        attr = [x.capitalize() for x in attr] # capitalize the first letter of the word
        attr = '_'.join(attr) # Join each word with "_"
        return(attr)

# Generate url
def generate_url(fixed_url, text , join_symbol):
    lower_text = text.lower().split()
    joined_text = join_symbol.join(lower_text)
    url = fixed_url + str(joined_text)
    return url


