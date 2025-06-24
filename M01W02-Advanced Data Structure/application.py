#TEXT CLASSIFICATION
#connect to file
a_file = open('data.txt', 'r')

#read content
data = a_file.read()

#preprocessing
data = data.replace('.', '')
data = data.replace(',', '')
data = data.lower()
data = data.split()

data = set(data)

#convert to dictionary - from text to number
dic_data = {value:index for index, value in enumerate(data)}

print(dic_data['a']) #output would be a number

#IMAGE IN COMPUTER VISION
#brayscale image
#color image
#binary image

#Calculate histogram