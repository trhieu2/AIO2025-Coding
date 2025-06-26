#motivation: measure similarity or gap between two strings
#minimum number of editing operations: delete, insert, substitution
def compute_levensthtein_distance(token1, token2):
    '''
    This function aims to calculate to minimum distance between two strings
    :param token1: first string
    :param token2: second string
    :return: int: the levensthtein distance
    '''
    distances = [[0] * (len(token2) + 1) for _ in range (len(token1) + 1)]

    for i in range(len(token1) + 1):
        distances[i][0] = i

    for j in range(len(token2) +1):
        distances[0][j] = j

    for i in range(1,len(token1) + 1):
        for j in range(1,len(token2) +1):
            if token1[i-1] == token2[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                a = distances[i-1][j] + 1
                b = distances[i][j-1] + 1
                c = distances[i-1][j-1] + 1
                distances[i][j] = min(a,b,c)

    return distances[len(token1)][len(token2)]


#Test
print(compute_levensthtein_distance('you', 'yu'))