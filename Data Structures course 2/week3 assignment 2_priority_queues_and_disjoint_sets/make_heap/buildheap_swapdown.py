# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = [] #array of tuples or arrays
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def swapdown(self,i):
        n = len(self._data)
        min_index = i
        l = 2*i+1 if (2*i+1<n) else -1 
        r = 2*i+2 if (2*i+2<n) else -1 
#         print(i,l,r)

        if l != -1 and self._data[l] < self._data[min_index]:
            min_index = l

        if r != - 1 and self._data[r] < self._data[min_index]:
            min_index = r

        if i != min_index:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = \
                self._data[min_index], self._data[i]
            self.swapdown(min_index)

    def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # efficient implementation is complete binary tree. but here you're not getting data 1 by 1, instead everything at once
    # so for i in range(0,n), implement swap up  ai < a2i+1  ai < a2i+2
        for i in range(len(self._data)//2 ,-1,-1):
            self.swapdown(i)
#             print('1')
#             for j in range(i + 1, len(self._data)):
#                 if self._data[i] > self._data[j]:
#                     self._swaps.append((i, j))
#                     self._data[i], self._data[j] = self._data[j], self._data[i]

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
