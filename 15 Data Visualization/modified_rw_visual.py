import matplotlib.pyplot as plt
from modified_random_walks import RandomWalk

# Keep making random walks as long as the program is active

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.

    plt.style.use("seaborn")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=1,
    )
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
    elif keep_running == "y":
        continue
    else:
        pass

