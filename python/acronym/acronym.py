import re
def abbreviate(target):
    # initialize the output
    output = ''

    # split the target string into words
    # for each of the target words...
    for target_word in re.split('[^a-zA-Z]', target):

        # append first character in upper case to the output
        output = output + target_word[0].upper()

    return output
