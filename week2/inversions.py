import argparse
import sys
from typing import List, Tuple


def main():

    # Parse command-line argument (file with integer list)
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file with integers")
    args = vars(parser.parse_args())

    # Read file and add integers to a list
    try:
        with open(args["file"], "r") as file:
            intList: List[int] = []

            for line in file:
                intList.append(int(line))
    except IOError:
        sys.exit(f"Could not read {args['file']}")

    print(f"Inversions: {sortAndCount(intList)[1]}")


def sortAndCount(intList: List[int]) -> Tuple[List[int], int]:
    if(len(intList) == 1):
        return intList, 0

    middle = len(intList) // 2
    leftList, leftInversions = sortAndCount(intList[:middle])
    rightList, rightInversions = sortAndCount(intList[middle:])

    mergedList, splitInversions = mergeAndCount(leftList, rightList)

    return mergedList, leftInversions + rightInversions + splitInversions


def mergeAndCount(leftList: List[int], rightList: List[int]) -> Tuple[List[int], int]:
    leftCopy = list(leftList)
    rightCopy = list(rightList)
    mergedList: List[int] = []
    inversionCount = 0

    while leftCopy and rightCopy:
        if leftCopy[0] <= rightCopy[0]:
            mergedList.append(leftCopy.pop(0))
        else:
            mergedList.append(rightCopy.pop(0))
            inversionCount += len(leftCopy)

    mergedList += (leftCopy or rightCopy)

    return mergedList, inversionCount


if __name__ == "__main__":
    main()
