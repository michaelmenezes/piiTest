import json, sys

output = []
line_no = 1
error_list = []

# print usage
def usage():
    print "Usage: piiTest.py <input_file>, <output_file>"

# Validate the number of arguments
if len(sys.argv) != 3:
    print "Error:"
    usage()
    print "Number of arguments: %d" %(len(sys.argv))
    exit(-1)

# return true if i is an integer and the number of digits is equal to size
def int_valid(i, size):
    if (len(i) == size):
        try:
            type(int(i)) == int
            return True
        except:
            return False
    return False

# validate the the area code with brackets around it is valid
def bracket_valid(d):
    if len(d) == 5:
        if d[0] == '(':
                if d[4] == ')':
                    try:
                        type(int(d[1:4])) == int
                        return True
                    except:
                        return False
    return False

#Validate that the phone number of valid. Supports 2 formats -
# with a space between the set of digits and with a bracket around the area code.
# Supports an area code that starts with a '0' based on the example.
# In reality there are no area codes in the US that with a '0' or a '1'
def phone_valid(n):
    #split based on space
    phone_list = n.split(' ')

    #check that there are 3 groups of digits
    if len(phone_list) == 3:
        if int_valid(phone_list[0], 3):
            if int_valid(phone_list[1], 3):
                if int_valid(phone_list[2], 4):
                    return True

    #split based on '-'
    phone_list = n.split('-')
    if len(phone_list) == 3:
        if bracket_valid(phone_list[0]):
            if int_valid(phone_list[1], 3):
                if int_valid(phone_list[2], 4):
                    return True
    return False

# Validate that the zip code is a 5 digit integer - US based
def zip_valid(z):
    if (len(z) == 5):
        try:
            type(int(z)) == int
            return True
        except:
            return False
    return False

# Validate that the color is a string
# As an enhancement it can a predefined set of colors. Right now blah is an acceptable color.
def color_valid(c):
    if type(c) == str:
        return True
    return False

input_file = open(sys.argv[1]) # open for read
output_file = open(sys.argv[2], "w")

for line in input_file:
    rec = {}
    list_rec = line.split(',')
    length = len(list_rec)
    if length == 5:
        list_rec[0] = list_rec[0].strip()
        if type(list_rec[0]) == str:
            list_rec[1] = list_rec[1].strip()
            if type(list_rec[1]) == str:
                list_rec[2] = list_rec[2].strip()
                if phone_valid(list_rec[2]):
                    if color_valid(list_rec[3]):
                        list_rec[4] = list_rec[4].strip()
                        if zip_valid(list_rec[4]):
                            #create a record in dict
                            rec["color"] = list_rec[3]
                            rec["firstname"] = list_rec[1]
                            rec["lastname"] = list_rec[0]
                            rec["phonenumber"] = list_rec[2].replace('(', '').replace(')', '').replace(' ', '-')
                            rec["zipcode"] = list_rec[4]
                            output.append(rec)
                            line_no += 1
                            continue
        error_list.append(line_no)
        line_no += 1

    elif length == 4:
        names = list_rec[0].split(' ')
        if len(names) == 2:
            names[0] = names[0].strip()
            if type(names[0]) == str:
                names[1] = names[1].strip()
                if type(names[1]) == str:
                    list_rec[1] = list_rec[1].strip()
                    if color_valid(list_rec[1]):
                        list_rec[2] = list_rec[2].strip()
                        if zip_valid(list_rec[2]):
                            list_rec[3] = list_rec[3].strip()
                            if phone_valid(list_rec[3]):
                                rec["color"] = list_rec[1]
                                rec["firstname"] = names[0]
                                rec["lastname"] = names[1]
                                rec["zipcode"] = list_rec[2]
                                rec["phonenumber"] = list_rec[3].replace('(', '').replace(')', '').replace(' ', '-')
                                output.append(rec)
                                line_no += 1
                                continue
        error_list.append(line_no)
        line_no += 1

    else:
        error_list.append(line_no)
        line_no += 1

out = {}
out['entries'] = sorted(output, key = lambda i: (i['firstname'], i['lastname']))
out['errors'] = error_list
output_file.write(json.dumps(out, indent = 2))





