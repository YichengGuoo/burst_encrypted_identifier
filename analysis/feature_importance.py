import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams["font.family"] = "Songti SC"
# plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["font.size"] = 22
label_font = {'family': 'Songti SC', 'weight': 'normal', 'size': 30}
legend_font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 22}
def feature_importance(importances, features):

    # show_features = []
    # show_importances = []
    # for i, x in enumerate(importances):
    #     if x > 0.01:
    #         show_importances.append(x)
    #         show_features.append(features[i])

    # Space-Time-Related features
    space_time_features = [i for i in range(41)]
    space_time_features.extend([53, 64, 65, 66, 67, 68, 69])
    # Authentication-Related features
    auth_features = [i for i in range(97, 127)]
    # Connection Management-Related features
    conn_features = [i for i in range(56, 63)]
    conn_features = [52, 127, 56, 57, 128, 129, 130, 132, 133, 132]
    # Encapsulation-Protocol-Related features
    encaps_features = [i for i in range(41, 52)]
    encaps_features.extend([54, 55, 131])
    # Obfuscation-Related features
    obfuscation_features = [i for i in range(70, 97)]

    features = {
        '时空特征': {'features': space_time_features, 'importance': 0},
        '认证模式': {'features': auth_features, 'importance': 0},
        '流量封装': {'features': encaps_features, 'importance': 0},
        '连接管理': {'features': conn_features, 'importance': 0},
        '流量混淆': {'features': obfuscation_features, 'importance': 0},
    }

    for i, x in enumerate(importances):
        for _, o in features.items():
            if i in o['features']:
                o['importance'] += x
                break

    show_importances = []
    show_features = []
    for n, o in features.items():
        print(f"the importance of feature {n} is {o['importance']}")
        show_features.append(n)
        show_importances.append(o['importance'])
    for i in range(len(show_importances)):
        show_importances[i] = show_importances[i] / len(features[show_features[i]]['features'])
        pass
    forest_importances = pd.Series(show_importances, index=show_features)
    fig, ax = plt.subplots(figsize=(16, 12))
    forest_importances.plot.bar(ax=ax, color='#ea7070')
    # ax.set_title("Feature importances using MDI")
    x_major_locator = MultipleLocator(0.005)
    ax.yaxis.set_major_locator(x_major_locator)
    ax.tick_params(labelsize=20)
    ax.set_xticklabels(["单位时空特征", "单位认证模式", "单位流量封装", "单位连接管理", "单位流量混淆"], fontdict=label_font)
    ax.set_ylabel("基尼重要性", fontdict=label_font)
    plt.xticks(rotation=0)
    fig.tight_layout()
    plt.savefig("./each_feature_importance.eps", bbox_inches='tight')
    plt.show()




