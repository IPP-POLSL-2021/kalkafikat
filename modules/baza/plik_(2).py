def quick_sort(arr: list[tuple[int, int]], left: int, right: int):
    # using arr[left] as pivot

    if left < right:
        m = left
        for i in range(left + 1, right + 1):
            if arr[i] < arr[left]:
                m += 1
                arr[m], arr[i] = arr[i], arr[m]
        arr[left], arr[m] = arr[m], arr[left]
        quick_sort(arr, left, m - 1)
        quick_sort(arr, m + 1, right)

# test class to use with pytest
class TestQuickSort:
    def test_1(self):
        tab = [(5, 10), (0, 1), (15, 15), (1, 4)]
        quick_sort(tab, 0, len(tab) - 1)
        assert tab == [(0, 1), (1, 4), (5, 10), (15, 15)]

    def test_2(self):
        tab = [(4, 9), (12, 2), (4, 7), (16, 3)]
        quick_sort(tab, 0, len(tab) - 1)
        assert tab == [(4, 7), (4, 9), (12, 2), (16, 3)]
