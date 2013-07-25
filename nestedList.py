data=[10,2,[12,13,14],22,33,[13,14,25,[11,10,9]]]
data1=[]
def ls(data):
    for elem in data:
        if isinstance(elem, list):
            ls(elem)
        else:
            data1.append(elem)
    return data1
print ls(data)