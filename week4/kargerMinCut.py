from argparse import ArgumentParser
from sys import exit
from typing import Dict, List, Tuple
from random import choice
from copy import deepcopy


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "file", help="file with integers representing vertices and edges of a graph")
    args = vars(parser.parse_args())

    try:
        with open(args["file"], "r") as file:
            graph: Dict[int, List[int]] = {}

            for line in file:
                lineItems: List[int] = list(map(int, line.split()))
                head, *tail = lineItems
                graph[head] = tail

    except IOError:
        exit(f"Could not read {args['file']}")

    print(f"Graph: {graph}")
    print(f"Input number of algorithm iterations (min 30 recommended):", end=' ')

    iterations = int(input())
    print(f"Found local minimum with {findBestMinCut(iterations, graph)} crossing edges")


def findBestMinCut(iterations: int, graph: Dict[int, List[int]]) -> int:
    crossingEdges = 2 * len(graph)
    bestMinCut = graph

    while iterations > 0:
        localGraph = deepcopy(graph)
        localMinimum = minCut(localGraph)

        finalVertices: List[int] = list(localMinimum.keys())
        minCrossingEdges = len(localMinimum[finalVertices[0]])

        if crossingEdges > minCrossingEdges:
            crossingEdges = minCrossingEdges
            bestMinCut = localMinimum

        print(f"Iteration {iterations}, crossingEdges: {crossingEdges}")
        iterations -= 1

    return crossingEdges


def minCut(graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
    if len(graph) <= 2:
        return graph

    contractVertices(choice(generateEdges(graph)), graph)
    return minCut(graph)


def contractVertices(chosenEdge: Tuple[int, int], graph: Dict[int, List[int]]) -> None:
    vertex1, vertex2 = chosenEdge
    finalEdges = list(filter(lambda v: v != vertex1 and v != vertex2,
                             list(graph[vertex1] + graph[vertex2])))

    del graph[vertex1], graph[vertex2]

    for vertex in graph:
        newEdges: List[int] = []
        for edge in graph[vertex]:
            if edge == vertex1 or edge == vertex2:
                newEdges.append(vertex1)
            else:
                newEdges.append(edge)
        graph[vertex] = newEdges

    graph[vertex1] = finalEdges


def generateEdges(graph: Dict[int, List[int]]) -> List[Tuple[int, int]]:
    edges: List[Tuple[int, int]] = []

    for vertex in graph:
        for neighbour in graph[vertex]:
            edges.append((vertex, neighbour))

    return edges


if __name__ == "__main__":
    main()
