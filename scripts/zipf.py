import argparse
from collections import Counter
from matplotlib import pyplot as plt

# ANSWERS TO QUESTIONS:
# (C) Roughly the shape of the graph is a straight line demonstrating that few words occur frequently and many occur infrequently.


def get_ranks_and_frequencies(infile):
    """Produces a list of rank, frequency pairs for each word in a text file
    :param infile: a text file
    :return: a list containing rank, frequency pairs for each word
    """
    with open(infile) as f:
        contents = f.read()
    c = Counter(contents.split())
    # TODO: create a list called ranks_and_frequencies that stores (rank,
    # frequency) pairs for each word in the file
    # c.items() accesses the element and count pairs to store in list

    # Order works by most frequent
    ordered_c = sorted(c.values(),reverse = True)
    # Give rank
    ranks_and_frequencies = list(enumerate(ordered_c))

    # --- RUN THIS CODE IF COMPETITION RANK ---
    # ordered_c = c.most_common()
    # i = 1
    # ranks_and_frequencies = []
    # previous_count = ordered_c[1]
    # for n in ordered_c:
      #  ranks_and_frequencies.append((i, n[1]))
        # if n[1] != previous_count:
        #    previous_count = n[1]
      #  i += 1
    # print(ranks_and_frequencies[0:20])

    return ranks_and_frequencies


def plot(infile):
    """
    Plots rank and frequency pairs to demonstrate Zipf's Law
    :param infile: a text file
    :return: None, produces a matplotlib plot
    """
    ranks_and_frequencies = get_ranks_and_frequencies(infile)

    # TODO: use the (rank, frequency) pairs to plot the data
    # and use a log scale on both axes
    # You will display the plot using plt.show(), which is already written

    # Separating x and y pairs to plot
    x = [count[0] for count in ranks_and_frequencies]
    y = [count[1] for count in ranks_and_frequencies]

    # Plot Zipf's Law graph
    plt.plot(x,y,'o')
    plt.title("Anna Kowalchyk")
    plt.xlabel("Rank (log scale)")
    plt.ylabel("Frequency (log scale)")

    # Setting axes to log scale
    plt.xscale("log")
    plt.yscale("log")

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Constructs a curve '
                                                 'demonstrating Zipf\'s Law '
                                                 'by plotting a rank, '
                                                 'frequency plot.')
    parser.add_argument('--path', type=str, required=True, help='Path to file')
    args = parser.parse_args()
    plot(args.path)
