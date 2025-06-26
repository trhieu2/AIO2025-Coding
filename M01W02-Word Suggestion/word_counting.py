import gdown
url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
output = 'file_path.ext'
gdown.download(url, output, quiet=False)

def preprocess_text(sentence):
    '''
    Preprocessing a sentence by:
    - Lowercasing
    - Excluding all (.) and (,)
    - Split into a list of words
    :param sentence(str): input sentence
    :return: list of words
    '''
    sentence = sentence.lower()
    sentence = sentence.replace('.','').replace(',','')
    words = sentence.split()
    return words

def word_count(file_path):
    '''
    Count the number of each word in the document after being preprocessed
    :param file_path
    :return: dict:
    '''
    with open(file_path, 'r') as f:
        document = f.read()
    words = preprocess_text(document)

    counter = {}
    for word in words:
        counter[word] = counter.get(word,0) + 1

    return counter

#Test
print(word_count('file_path.ext'))