import merge_sort

def test_merge_sort() -> None:
    test_array = [6,5,4,3,2,1]
    sorted = merge_sort.Merge_Sort(test_array, 0, 5)
    answer = [1,2,3,4,5,6]
    assert sorted == answer
    print(sorted)
    print(answer)