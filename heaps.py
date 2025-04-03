# Lets code a heap data structure in Python

class Heap:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.size = 0
        self.heap = [None] * (max_size + 1)  # Index 0 is not used

    def insert(self, value: int) -> None:
        if self.size >= self.max_size:
            raise Exception("Heap is full")
        self.size += 1
        self.heap[self.size] = value
        self._heapify_up(self.size)

    def _heapify_up(self, index: int) -> None:
        while index > 1:
            parent_index = index // 2
            if self.heap[index] > self.heap[parent_index]:
                # Swap the values
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index],
                )
                index = parent_index
            else:
                break


    def extract_max(self) -> int:
        if self.size == 0:
            raise Exception("Heap is empty")
        max_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self._heapify_down(1)
        return max_value
    
    def _heapify_down(self, index: int) -> None:
        while index * 2 <= self.size:
            left_child_index = index * 2
            right_child_index = left_child_index + 1
            largest_index = index

            if self.heap[left_child_index] > self.heap[largest_index]:
                largest_index = left_child_index
            if right_child_index <= self.size and self.heap[right_child_index] > self.heap[largest_index]:
                largest_index = right_child_index

            if largest_index != index:
                # Swap the values
                self.heap[index], self.heap[largest_index] = (
                    self.heap[largest_index],
                    self.heap[index],
                )
                index = largest_index
            else:
                break

    def peek(self) -> int:
        if self.size == 0:
            raise Exception("Heap is empty")
        return self.heap[1]
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def __str__(self) -> str:
        return str(self.heap[1:self.size + 1])
    
# Example usage
if __name__ == "__main__":
    heap = Heap(10)
    heap.insert(5)
    heap.insert(10)
    heap.insert(3)
    heap.insert(8)
    print("Heap after insertions:", heap)  # Should print the heap in array form
    print("Max value extracted:", heap.extract_max())  # Should print 10
    print("Heap after extraction:", heap)  # Should print the heap after extraction
    print("Peek max value:", heap.peek())  # Should print the new max value
    print("Is heap empty?", heap.is_empty())  # Should print False
    heap.extract_max()  # Extract remaining elements
    heap.extract_max()  # Extract remaining elements
    print("Is heap empty?", heap.is_empty())  # Should print True