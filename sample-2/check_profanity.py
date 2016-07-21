import urllib

def read_text():

    # extract content from the file
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    # print(contents_of_file)
    quotes.close()

    # convert to pirate speech
    convert_to_private_speech(contents_of_file)

    # check profanity
    check_profanity(contents_of_file)

def check_profanity(content):

    # perform url get to check profanity
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + content)
    output = connection.read()
    # print(output)
    connection.close()

    if "true" in output:
        print "Profanity Alert!!"
    elif "false" in output:
        print "This document has no curse words"
    else:
        print "Unable to scan the document"

def convert_to_private_speech(content):

    # perform url get to check profanity
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + content)
    output = connection.read()
    print(output + "\n")
    connection.close()
    

read_text()





