from collatex import *
import re

# Ignore <pb> elements
# Ignore comments

def tokenize(input):
    # words = re.findall(r'\w+\s*|\W+', input)
    words = re.findall(r'%|<paragraph/>|<pb.+?/>|<note>.+?</note>|<!--.+?-->|[\w</>]+\s*|[^\w%]+', input)
    tokens = []
    [tokens.append({"t": token}) for token in words] # create dictionaries for each token
    return tokens


with open('1818_Ch1.txt', 'r') as f1818file, \
    open('1823_Ch1.txt', 'r') as f1823file, \
    open('1831_Chs1-2.txt', 'r') as f1831file:
    f1818 = f1818file.read()
    f1823 = f1823file.read()
    f1831 = f1831file.read()
    f1818_paragraphed = re.sub(r'\n\n',r'<paragraph/>',f1818)
    f1818_tokens = tokenize(f1818_paragraphed)

# collation = Collation()

print(f1818_tokens)
