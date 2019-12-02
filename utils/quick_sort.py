
class QuickSort():
    def __init__(self, data):
        self.data = list(data)

    def swap(self, left, right):
        temp = self.data[left]
        self.data[left] = self.data[right]
        self.data[right] = temp

    def partition(self, left, right):
        if left >= right:
            return None

        pivot = right
        right -= 1
        while left < right:
            if self.data[right] < self.data[pivot]:
                self.swap(left, right)
                left += 1
            else:
                right -= 1
        if self.data[left] < self.data[pivot]:
            self.swap(left + 1, pivot)
            return left + 1
        else:
            self.swap(left, pivot)
            return left

    def partition_forward(self, left, right):
        if left >= right:
            return None

        pivot = left
        left += 1
        while left < right:
            if self.data[left] > self.data[pivot]:
                self.swap(left, right)
                right -= 1
            else:
                left += 1
        if self.data[left] > self.data[pivot]:
            self.swap(left - 1, pivot)
            return left - 1
        else:
            self.swap(left, pivot)
            return left

    def sort(self, left=0, right=None):
        if right is None:
            right = len(self.data) - 1
        if left == right:
            return self.data
        pivot = self.partition(left, right)
        if pivot is not None:
            self.sort(left, pivot - 1)
            self.sort(pivot + 1, right)
        return self.data

    def select(self, n, left=0, right=None):
        if right is None:
            right = len(self.data) - 1
        if left == right:
            return self.data
        pivot = self.partition(left, right)
        if pivot > n:
            self.select(n, left, pivot - 1)
            return self.data[n]
        elif pivot < n:
            self.select(n, pivot + 1, right)
            return self.data[n]
        else:
            return self.data[n]
