class BinHeap:
    def __init__(self):
        self.binheap = [0]
        self.size = 0
    
    def insertBH(self, i):
        self.binheap.append(i)
        self.size += 1
        k = self.size
        while True:
            if k % 2: # 홀수 일때
                if self.binheap[k] < self.binheap[k//2]:
                    self.binheap[k], self.binheap[k//2] = self.binheap[k//2], self.binheap[k]
                    k = k // 2
                else: break
            else:
                if self.binheap[k] > self.binheap[k//2] :
                    self.binheap[k], self.binheap[k//2] = self.binheap[k//2], self.binheap[k]
                    k = k // 2
                else: break 
                
for tc in range(1, int(input())+1):
    n = int(input())
    bh = BinHeap()
    for nod in range(1, n+1):
        bh.insertBH(nod)
        print(bh.binheap)
    print('#{} {} {}'.format(tc, bh.binheap[1], bh.binheap[n//2]))        
