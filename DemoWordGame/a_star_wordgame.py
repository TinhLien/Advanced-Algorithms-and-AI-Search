from WordGameNode import WordGameNode
from WordGameNode import read_dictionary
from WordGameNode import check_valid_words
import sys


def a_star_search(start, goal):
    todo = [start]
    visited = set()
    num_searches = 0
    while len(todo) > 0:
        next = todo.pop(0)  # Get (and remove) first element in the list (using the list as a queue)
        num_searches += 1

        sys.stdout.flush()
        sys.stdout.write("\r\rNumber of searches: {0}".format(num_searches))

        if next == goal:
            return num_searches, next
        else:
            # Keep searching.
            visited.add(next)  # Remember that we've been here

            # Add children to the todo list and update the score
            for child in next.get_children():
                if child not in visited and child not in todo:
                    child.score = child.depth + child.heuristic(goal)
                    # score = g(n) + h(n)
                    todo.append(child)

            # Sort the children by score (lowest better)
            todo.sort(key=lambda x: x.score)

    return num_searches, None  # no route to goal


def main(args):
    if len(args) == 4:
        start_word = args[1]
        goal_word = args[2]
        word_file_path = args[3]
    elif len(args) == 3:
        start_word = args[1]
        goal_word = args[2]
        word_file_path = "./10k.txt"
    else:
        print("*** Please enter words of the same length. ***")
        valid = False
        while not valid:
            start_word = input("Enter the start word: ").strip()
            goal_word = input("Enter the goal word: ").strip()
            if len(start_word) == len(goal_word):
                valid = True
            else:
                print("*** Words not of the same length! Please re-enter ***")
        word_file_path = input("Enter a file path containing words to search, leave blank to use default: ").strip()
        if not word_file_path:
            word_file_path = "./20k.txt"
    print()

    # This reads the dictionary and updates the valid_words
    # global variable for WordGameNode.
    read_dictionary(word_file_path, len(start_word))
    if not check_valid_words(start_word):
        print("\"{}\" not in word file!".format(start_word))
    elif not check_valid_words(goal_word):
        print("\"{}\" not in word file!".format(goal_word))
    else:
        start = WordGameNode(start_word)
        goal = WordGameNode(goal_word)

        num_searches, node = a_star_search(start, goal)
        # Do the A star search
        if not node:
            print("\nThere is no path from {0} to {1}".format(start, goal))
            print("Number of searches: {0}".format(num_searches))
        else:
            print("\nPath from start word to goal word: ")
            print(" -> ".join(reversed([str(word) for word in node.get_path()])))


if __name__ == "__main__":
    main(sys.argv)