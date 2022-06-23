import csv
import queue as q


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


# Implement this function to read data into an appropriate data structure.
def build_graph(path):
    graph = {}  # Initialize an empty dictionary. Because we will return the graph as a dictionary.

    with open(path, "r", encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if reader.line_num != 1:  # To skip the header in the csv file.
                if row[0] not in graph:
                    graph[row[0]] = {}  # Inner dictionary to hold the neighbors as keys.
                if row[1] not in graph:
                    graph[row[1]] = {}  # Inner dictionary to hold the neighbors as keys.

                # Giving costs of paths as values to the inner dictionary.
                graph[row[0]][row[1]] = int(row[2])
                graph[row[1]][row[0]] = int(row[2])

        print("*******************************")
        print(graph)
        print("*******************************")
        return graph


# Implement this function to perform uniform cost search on the graph.
def uniform_cost_search(graph, start, end):

    # It raises CityNotFound exception and it perceives the city parameter which doesn't in the graph.
    if start not in graph:
        raise CityNotFoundError(start)
    if end not in graph:
        raise CityNotFoundError(end)

    # Used priority queue because FIFO principle won't help us in this case.
    queue = q.PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        # Priority queue will remove the item in the ascending order thus we will get the minimum cost.
        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Total distance = " + str(node[0]))
            break

        cost = node[0]
        # To get the next step via using Uniform Cost Search
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))


# Implement main to call functions with appropriate try-except blocks

if __name__ == "__main__":

    try:
        path = str(input("Please enter the path of the road map file: "))
        start = str(input("Please enter the current city. (Pay attention to the capital letter): "))
        end = str(input("Please enter the target city. (Pay attention to the capital letter): "))
        graph = build_graph(path)
        uniform_cost_search(graph, start, end)

    except FileNotFoundError:
        print("FileNotFoundError")
    except CityNotFoundError:
        pass
    except Exception:
        print("An exception occured")

