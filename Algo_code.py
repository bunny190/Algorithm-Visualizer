import tkinter as tk
import random
import time

class AlgoVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title('Algorithm Visualizer')
        self.canvas = tk.Canvas(root, width=800, height=400, bg='white')
        self.canvas.pack()
        self.data = []
        self.speed = 0.1

        self.create_controls()
        self.generate_data()

    def create_controls(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Generate Data", command=self.generate_data).pack(side='left')
        tk.Button(frame, text="Bubble Sort", command=self.bubble_sort).pack(side='left')
        tk.Button(frame, text="Selection Sort", command=self.selection_sort).pack(side='left')
        tk.Button(frame, text="Merge Sort", command=lambda: self.merge_sort(0, len(self.data) - 1)).pack(side='left')
        tk.Button(frame, text="Heap Sort", command=self.heap_sort).pack(side='left')
        tk.Button(frame, text="Binary Search", command=lambda: self.binary_search(25)).pack(side='left')

    def generate_data(self):
        self.data = [random.randint(10, 100) for _ in range(30)]
        self.draw_data()

    def draw_data(self, color_array=None):
        self.canvas.delete("all")
        c_width, c_height = 800, 400
        bar_width = c_width / len(self.data)
        max_height = max(self.data)

        for i, val in enumerate(self.data):
            x0 = i * bar_width
            y0 = c_height - (val / max_height * 350)
            x1 = (i + 1) * bar_width
            y1 = c_height
            color = color_array[i] if color_array else 'blue'
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.root.update_idletasks()

    def bubble_sort(self):
        for i in range(len(self.data)):
            for j in range(len(self.data) - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_data(['green' if x == j or x == j + 1 else 'blue' for x in range(len(self.data))])
                    time.sleep(self.speed)
        self.draw_data(['green'] * len(self.data))

    def selection_sort(self):
        for i in range(len(self.data)):
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
                self.draw_data(['red' if x == j or x == min_idx else 'blue' for x in range(len(self.data))])
                time.sleep(self.speed)
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
        self.draw_data(['green'] * len(self.data))

    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)
            self.draw_data(['purple' if left <= x <= right else 'blue' for x in range(len(self.data))])
            time.sleep(self.speed)

    def merge(self, left, mid, right):
        L = self.data[left:mid+1]
        R = self.data[mid+1:right+1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                self.data[k] = L[i]
                i += 1
            else:
                self.data[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            self.data[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            self.data[k] = R[j]
            j += 1
            k += 1

    def heapify(self, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and self.data[l] > self.data[largest]:
            largest = l
        if r < n and self.data[r] > self.data[largest]:
            largest = r
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.draw_data(['orange' if x == i or x == largest else 'blue' for x in range(len(self.data))])
            time.sleep(self.speed)
            self.heapify(n, largest)

    def heap_sort(self):
        n = len(self.data)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(n, i)
        for i in range(n-1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(i, 0)
        self.draw_data(['green'] * len(self.data))

    def binary_search(self, target):
        self.data.sort()
        self.draw_data()
        low = 0
        high = len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            self.draw_data(['red' if i == mid else 'blue' for i in range(len(self.data))])
            time.sleep(self.speed)
            if self.data[mid] == target:
                self.draw_data(['green' if i == mid else 'blue' for i in range(len(self.data))])
                return
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

if __name__ == "__main__":
    root = tk.Tk()
    app = AlgoVisualizer(root)
    root.mainloop()
