import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import Axes


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 22
label_font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 28}
legend_font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 22}
# plt.style.use('bmh')



def curvelinear(fig, t, data, title):
    ax1 = fig.add_subplot(1, 1, 1, axes_class=Axes)
    # ax1 will have ticks and gridlines defined by the given transform (+
    # transData of the Axes).  Note that the transform of the Axes itself
    # (i.e., transData) is not affected by the given transform.
    markers = ["s", "8", "^", "*", "P", "H", "h"]
    color = ['#2694ab', (196/255, 151/255, 178/255), (107/255, 112/255, 92/255)]

    for i, (label, s) in enumerate(data.items()):
        ax1.plot(t, s, label=label, marker=markers[i], color=color[i], linewidth=4, markersize=12)


    # create new axis to set coorp in each line
    # ax1.axis["t2"] = ax1.new_floating_axis(1, 1, axis_direction="left")
    # ax1.axis["t3"] = ax1.new_floating_axis(1, 2, axis_direction="left")
    # ax1.axis["t4"] = ax1.new_floating_axis(1, 3, axis_direction="left")
    # ax1.axis["t5"] = ax1.new_floating_axis(1, 4, axis_direction="left")
    # ax1.axis["t6"] = ax1.new_floating_axis(1, 5, axis_direction="left")
    # ax1.axis["t7"] = ax1.new_floating_axis(1, 6, axis_direction="left")
    # plt.grid(alpha=0.3, axis='both', color="black", linestyle='dashed')
    x_major_locator = MultipleLocator(0.1)
    ax1.set_ylim(0.59, 1.01)
    ax1.set_xlim(-0.03, 6.03)
    ax1.yaxis.set_major_locator(x_major_locator)
    # plt.title(title)
    plt.legend(ncols=3, bbox_to_anchor=(0, 1),
              loc='lower left', prop=legend_font)

def plot_cm():
    data = [[650, 3, 7, 3, 15],
            [2, 626, 15, 5, 20],
            [0, 8, 646, 8, 30],
            [1, 6, 25, 712, 5],
            [3, 29, 33, 2, 717]]
    data = np.array(data)
    classes =["WECHAT", "QQ", "WEB", "SIP", "SCP", "CHAT", "SSH"]
    # plot_confusion_matrix(data, classes, "confusion matrix", plt.cm.Blues, normalize='true')


def plot_method_metrics():

    methods = ("C4.5", "Random Forest", "1D-CNN", "2D-CNN", "Burst-CNN-LSTM", "Burst-ATT-LSTM", "Burst-ATT-BiLSTM")
    method_metric_5 = {
        'Accuracy': (0.9303, 0.9443, 0.9555, 0.9372, 0.9456, 0.9667, 0.9752),
        'Precision': (0.9319, 0.9437, 0.9374, 0.8931, 0.9444, 0.9645, 0.9745),
        'Recall': (0.9364, 0.9389, 0.9088, 0.8856, 0.9288, 0.9650, 0.9688),
        'F1-score': (0.9390, 0.9422, 0.9217, 0.8892, 0.9357, 0.9621, 0.9715)
    }
    method_metric_7 = {
        'Accuracy': (0.9663, 0.9662, 0.9441, 0.9336, 0.9425, 0.9640, 0.9761),
        'Precision': (0.9325, 0.9563, 0.6986, 0.7382, 0.9427, 0.9609, 0.9738),
        'Recall': (0.8681, 0.8646, 0.6561, 0.6611, 0.9314, 0.9569, 0.9723),
        'F1-score': (0.8986, 0.9025, 0.6679, 0.6776, 0.9365, 0.9587, 0.9729)
    }

    x = np.arange(len(methods))  # the label locations
    width = 0.15  # the width of the bars
    multiplier = 0
    colors = ['red', 'tan', 'lime']
    fig = plt.figure(figsize=(16, 12))
    ax = fig.add_subplot()
    # fig, ax = plt.subplots(layout='constrained', figures=(10, 5))
    # rects1 = ax.bar(x - width * 1.5, method_metric_7['Accuracy'], width, label='Accuracy', ec='k', lw=.8,)
    rects1 = ax.bar(x - width * 1.5, method_metric_7['Accuracy'], width, label='Accuracy',
                    fc='#E8DFCA', edgecolor='k')
    rects1 = ax.bar(x - width / 2, method_metric_7['Precision'], width, label='Precision',
                        fc='#AEBDCA', edgecolor='k')
    rects2 = ax.bar(x + width / 2, method_metric_7['Recall'], width, label='Recall',
                    fc='#F5EFE6', edgecolor='k')
    rects2 = ax.bar(x + width * 1.5, method_metric_7['F1-score'], width, label='F1-score',
                    fc='#7895B2', edgecolor='k')

    # rects2 = ax.bar(x - width - 0.25, penguin_means['Precision'], width, label='2016', ec='k', color='lime',
    #                 lw=.8, hatch='***')
    # rects3 = ax.bar(x + 0.25, penguin_means['Precision'], width, label='2016', ec='k', color='tan',
    #                 lw=.8, hatch='***')
    # rects2 = ax.bar(x + width + 0.75, penguin_means['Precision'], width, label='2016', ec='k', color='lime',
    #                 lw=.8, hatch='***')

    # for attribute, measurement in penguin_means.items():
    #     offset = width * multiplier
    #     rects = ax.bar(x + offset, measurement, width, label=attribute)
    #     # ax.bar_label(rects, padding=3)
    #     multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    # ax.set_ylabel('Length (mm)')
    # ax.set_title('Penguin attributes by species')
    ax.set_xticks(x, methods)
    ax.legend(ncols=4, bbox_to_anchor=(0, 1),
              loc='lower left', prop=legend_font)
    ax.set_ylim(0.60, 1.0005)
    x_major_locator = MultipleLocator(0.05)
    ax.yaxis.set_major_locator(x_major_locator)
    plt.xticks(rotation=23)
    plt.savefig("./method-metric-7.eps", bbox_inches='tight')
    plt.show()


def plot_model_metrics():
    t = ["QQ", "WECHAT",  "WEB", "SIP", "SCP", "CHAT", "SSH"]
    accuracys = {
        # "Burst-LSTM": [0.93, 0.88, 0.88, 1.0, 0.82, 0.88, 0.98],
        "Burst-CNN-LSTM": [0.97, 0.86, 0.95, 0.94, 0.96, 0.91, 0.93],
        # "Burst-BiLSTM": [0.97, 0.94, 0.92, 0.98, 0.86, 0.92, 0.98],
        "Burst-ATT-LSTM": [0.98, 0.93, 0.97, 0.96, 0.96, 0.96, 0.94],
        "Burst-ATT-BiLSTM": [0.99, 0.95, 0.98, 0.98, 0.99, 0.97, 0.96]
    }
    precisions = {
        # "Burst-LSTM": [0.93, 0.88, 0.88, 1.0, 0.82, 0.88, 0.98],
        "Burst-CNN-LSTM": [0.96, 0.94, 0.91, 0.98, 0.93, 0.90, 0.98],
        "Burst-ATT-LSTM": [0.98, 0.96, 0.95, 0.99, 0.92, 0.95, 0.98],
        # "Burst-BiLSTM": [0.97, 0.94, 0.92, 0.98, 0.86, 0.92, 0.98],
        "Burst-ATT-BiLSTM": [0.99, 0.98, 0.96, 0.98, 0.95, 0.97, 0.99]

    }
    recalls = {
        # "Burst-LSTM": [0.93, 0.92, 0.93, 0.90, 0.87, 0.88, 0.94],
        "Burst-CNN-LSTM": [0.97, 0.85, 0.95, 0.94, 0.96, 0.90, 0.93],
        "Burst-ATT-LSTM": [0.98, 0.93, 0.97, 0.96, 0.96, 0.96, 0.94],
        # "Burst-BiLSTM": [0.96, 0.96, 0.95, 0.96, 0.84, 0.91, 0.94],
        "Burst-ATT-BiLSTM": [0.99, 0.95, 0.98, 0.98, 1.0, 0.96, 0.96],

    }
    f_score = {
         # "Burst-LSTM": [0.93, 0.90, 0.91, 0.95, 0.84, 0.88, 0.96],
        "Burst-CNN-LSTM": [0.97, 0.90, 0.93, 0.96, 0.95, 0.90, 0.95],
        "Burst-ATT-LSTM": [0.98, 0.95, 0.96, 0.98, 0.94, 0.96, 0.96],
        # "Burst-BiLSTM": [0.97, 0.95, 0.93, 0.97, 0.85, 0.92, 0.96],
        "Burst-ATT-BiLSTM": [0.99, 0.96, 0.97, 0.98, 0.97, 0.97, 0.97],

    }
    fig = plt.figure(figsize=(16, 11))
    # fig = plt.figure()
    
    # curvelinear(fig, t, accuracys, "Accuracy")
    # curvelinear(fig, t, precisions, "Precision")
    # curvelinear(fig, t, recalls, "Recall")
    curvelinear(fig, t, f_score, "F-score")
    # curvelinear(fig, t, precisions_10_20_30, "Precision")
    # curvelinear(fig, t, recalls_10_20_30, "Recall")
    # curvelinear(fig, t, f_scores_10_20_30, "F-score")
    # plot_cm()

    plt.grid(linestyle=(0, (1, 10)), linewidth=3)
    plt.savefig("./burst-model-fscore.eps", bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    # plot_method_metrics()
    plot_model_metrics()
