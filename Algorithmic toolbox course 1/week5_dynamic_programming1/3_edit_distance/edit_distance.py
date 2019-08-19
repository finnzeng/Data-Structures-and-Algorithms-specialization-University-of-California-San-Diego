# Uses python3
import numpy
def edit_distance(s1, s2):
    len_1 = len(s1)
    len_2 = len(s2)

    dpresult = numpy.zeros((len_1+1 , len_2+1)) # a martix
    for i in range(len_2+1):  # edit distance for a null string and another string is just length of string
        dpresult[0][i] = i

    for i in range(len_1+1):
        dpresult[i][0] = i

    # Filling remaining matrix
    for i in range(1, len_1+1):
        for j in range(1, len_2+1):
            insertion = dpresult[i][j-1] + 1
            deletion  = dpresult[i-1][j] + 1
            mismatch  = dpresult[i-1][j-1] + 1
            match     = dpresult[i-1][j-1]
            if s1[i-1] == s2[j-1]: #when it matches
                dpresult[i][j] = min(insertion, deletion, match)
            if s1[i-1] != s2[j-1]: #when it doesn't match
                dpresult[i][j] = min(insertion, deletion, mismatch)
    
    return (int(dpresult[len_1][len_2]))
if __name__ == "__main__":
    print(edit_distance(input(), input()))
