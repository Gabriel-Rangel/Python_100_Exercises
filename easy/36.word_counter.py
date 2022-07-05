#Please download the words1.txt file from the attachment and 
# then create a Python function that takes a text file as input and 
# returns the number of words contained in the text file.



def count_words(file_name):
    with open(file_name, 'r') as f:
        return len(f.read().split())

print(count_words("easy\words1.txt"))