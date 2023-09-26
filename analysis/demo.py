import numpy as np
from matplotlib import pyplot as plt


def repeat(x, count):
    return [x for i in range(count)]


def draw_demo_flow():
    import numpy as np
    import matplotlib.pyplot as plt

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    plt.style.use('bmh')

    def plot_beta_hist(ax, a, b):
        ax.bar(np.random.beta(a, b, size=10000), bins=25, alpha=0.8, density=True)

    fig, ax = plt.subplots()
    data1 = [(1, 10), (2, 70), (3, 80), (4, 100), (5, 93), (6, 92), (7, 90), (8, 70), (9, 60), (10, 20),
             (11, 30), (12, 50), (13, 70), (14, 70), (15, 70), (16, 80), (17, 80), (18, 70), (19, 60), (20, 60),
             (21, 50), (22, 10), (23, 10), (24, 20), (25, 30), (26, 45), (27, 20), (28, 0), (29, 0), (30, 0),
             (31, 40), (32, 70), (33, 60), (34, 40), (35, 78), (36, 88), (37, 89), (38, 92), (39, 88), (40, 77),
             (41, 84), (42, 88), (43, 89), (44, 94), (45, 30), (46, 20), (47, 20), (48, 30), (49, 50), (50, 30),
             (51, 20), (52, 22), (53, 0), (54, 0), (55, 0), (56, 0), (57, 0), (58, 0), (59, 70), (50, 60),
             (61, 40), (62, 30), (63, 40), (64, 80), (65, 70), (66, 72), (67, 73), (68, 72), (69, 90), (70, 85),
             (71, 60), (72, 20), (73, 30), (74, 30), (75, 40), (76, 60), (77, 70), (78, 70), (79, 72), (80, 69),
             (81, 30), (82, 40), (83, 50), (84, 40), (85, 30), (86, 30), (87, 10), (88, 0), (89, 20), (90, 10),
             (91, 10), (92, 17), (93, 28), (94, 38), (95, 48), (96, 58), (97, 60), (98, 70), (99, 30), (100, 20)

             ]
    x1 = []
    for p in data1:
        x1.extend(repeat(*p))
    ax.hist(x1, histtype="stepfilled", bins=100, alpha=0.8)
    # plt.tight_layout()
    plt.show()


def test():
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(19680801)

    fig, ax = plt.subplots()
    x = 30 * np.random.randn(10000)
    mu = x.mean()
    median = np.median(x)
    sigma = x.std()
    textstr = '\n'.join((
        r'$\mu=%.2f$' % (mu,),
        r'$\mathrm{median}=%.2f$' % (median,),
        r'$\sigma=%.2f$' % (sigma,)))
    print(x)
    ax.hist(x, 50)
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # place a text box in upper left in axes coords
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)

    plt.show()


if __name__ == "__main__":
    draw_demo_flow()
