class MaxHeap:

    def __init__(self, *args):
        self.heap = []
        self.heap_size = 0
        for i in args:
            self.heap.append(i)
            self.heap_size += 1
            self.sift_up(self.heap_size - 1)

    def sift_down(self, i):
        while 2 * i + 1 < self.heap_size:
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < self.heap_size and \
                    self.heap[right] > self.heap[left]:
                j = right
            if self.heap[i] >= self.heap[j]:
                break;

            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def sift_up(self, i):
        while self.heap[i] > self.heap[(i - 1) // 2] and i > 0:
            self.heap[i], self.heap[(i - 1) // 2] = \
                self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def extract_max(self):
        max_elem = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap.pop()
        self.heap_size -= 1
        self.sift_down(0)
        return max_elem

    def insert(self, key):
        self.heap_size += 1
        self.heap.append(key)
        self.sift_up(self.heap_size - 1)

    def show(self):
        return self.heap


def main():
    n = int(input())
    heap = MaxHeap()
    for i in range(n):
        s = input()
        if s[0] == "I":
            heap.insert(int(s.split()[1]))
        else:
            print(heap.extract_max())


if __name__ == '__main__':
    main()
