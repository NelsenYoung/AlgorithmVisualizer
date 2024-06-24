import merge_sort

def test_merge_sort() -> None:
    test_array = [3,4,6,1,2,5]
    sorted = merge_sort.Merge_Sort(test_array, 1, 6)
    answer = [1,2,3,4,5,6]
    assert sorted == answer
    print(sorted)
    print(answer)