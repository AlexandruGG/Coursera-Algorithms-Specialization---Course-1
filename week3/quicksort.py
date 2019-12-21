from argparse import ArgumentParser
from sys import exit
from typing import List
from statistics import median


def main():
    # Parse command-line argument (file with integer list)
    parser = ArgumentParser()
    parser.add_argument("file", help="file with integers")
    args = vars(parser.parse_args())

    # Read file and add integers to a list
    try:
        with open(args["file"], "r") as file:
            intList: List[int] = [int(line) for line in file]
    except IOError:
        exit(f"Could not read {args['file']}")

    print(f"Which pivot would you like to use?")
    print(f"1. First element of array")
    print(f"2. Last element of array")
    print(f"3. Median between first, middle, and last element of array")
    print(f"Choose option number:", end=' ')

    option = int(input())
    print(f"Number of comparisons made: {quickSort(intList, option)[1]}")


def quickSort(intList: List[int], option: int) -> Tuple[List[int], int]:
    length = len(intList)
    if length <= 1:
        return intList, 0

    p = choosePivot(intList, option)
    intList[0], intList[p] = intList[p], intList[0]

    intList, pivotPosition = partition(intList)
    intList[:pivotPosition], leftComparisons = quickSort(intList[:pivotPosition], option)
    intList[pivotPosition + 1:], rightComparisons = quickSort(intList[pivotPosition + 1:], option)

    return intList, leftComparisons + rightComparisons + length - 1


def choosePivot(intList: List[int], option: int) -> int:
    listLength = len(intList)
    middlePosition = (listLength // 2) - 1 if listLength % 2 == 0 else listLength // 2

    firstElement = intList[0]
    middleElement = intList[middlePosition]
    lastElement = intList[listLength - 1]

    threeElemList = [firstElement, middleElement, lastElement]
    medianPivot = int(median(threeElemList))

    if option == 1:
        return 0
    elif option == 2:
        return listLength - 1
    elif option == 3:
        return intList.index(medianPivot)
    else:
        exit(f"Option {option} is invalid!")


def partition(intList: List[int]) -> Tuple[List[int], int]:
    pivot = intList[0]
    i = 1

    for j in range(1, len(intList)):
        if intList[j] < pivot:
            intList[i], intList[j] = intList[j], intList[i]
            i += 1

    intList[0], intList[i-1] = intList[i-1], intList[0]
    return intList, i-1


if __name__ == "__main__":
    main()
