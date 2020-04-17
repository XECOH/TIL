class BinHeap:
    def __init__(self):
        self.binheap = [0]
        self.size = 0
        self.ansbinheap = []
    
    def insertBH(self, i):
        self.binheap.append(i)
        self.size += 1
        k = self.size
        while k // 2 > 0:
            if self.binheap[k] > self.binheap[k//2]:
                self.binheap[k], self.binheap[k//2] = self.binheap[k//2], self.binheap[k]
                k = k // 2
            else: break
    
    def deleteBH(self):
        if len(self.binheap) == 1:
            self.ansbinheap += [-1]
        else:
            retval = self.binheap[1]
            self.ansbinheap += [retval]
            self.binheap[self.size], self.binheap[1] = self.binheap[1], self.binheap[self.size]
            self.binheap.pop()
            self.size -= 1
            self.percDown(1)
    
    def maxChild(self, i):
        if (i * 2) + 1 > self.size:
            return i * 2
        else:
            if self.binheap[i * 2] > self.binheap[(i * 2) + 1]:
                return i * 2
            else:
                return (i * 2) + 1
    
    def percDown(self, i):
        while i * 2 <= self.size:
            mc = self.maxChild(i)
            if self.binheap[i] < self.binheap[mc]:
                self.binheap[i], self.binheap[mc] = self.binheap[mc], self.binheap[i]
            i = mc

for tc in range(1, int(input())+1):
    bh = BinHeap()
    n = int(input())
    for _ in range(n):
        orders = list(map(int, input().split()))
        if orders[0] == 1:
            bh.insertBH(orders[1])
        else:
            bh.deleteBH()
    print('#{} {}'.format(tc, ' '.join(map(str, bh.ansbinheap))))

