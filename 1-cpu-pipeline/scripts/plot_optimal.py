import numpy as np
import matplotlib.pyplot as plt

def optimal():
    point = 1.214

    x_perf_0 = np.linspace(point, 1.6, 40)
    y_perf_0 = 2 * x_perf_0
    x_perf_1 = np.linspace(1.6, 2.2, 60)
    y_perf_1 = 2 * x_perf_1 * (x_perf_1 / 2 + 0.2) ** 2

    x_perf = np.concatenate((x_perf_0, x_perf_1))
    y_perf = np.concatenate((y_perf_0, y_perf_1))

    x_eff_0 = np.linspace(0, 0.8, 80)
    y_eff_0 = x_eff_0
    x_eff_1 = np.linspace(0.8, point, 40)
    y_eff_1 = x_eff_1 * (x_eff_1 + 0.2) ** 2

    x_eff = np.concatenate((x_eff_0, x_eff_1))
    y_eff = np.concatenate((y_eff_0, y_eff_1))

    x = np.concatenate((x_eff, x_perf))
    y = np.concatenate((y_eff, y_perf))
    return (x, y)

def original():
    x_perf_0 = np.linspace(0, 1.6, 160)
    y_perf_0 = 2 * x_perf_0
    x_perf_1 = np.linspace(1.6, 2.2, 60)
    y_perf_1 = 2 * x_perf_1 * (x_perf_1 / 2 + 0.2) ** 2

    x_perf = np.concatenate((x_perf_0, x_perf_1))
    y_perf = np.concatenate((y_perf_0, y_perf_1))

    x_eff_0 = np.linspace(0, 0.8, 80)
    y_eff_0 = x_eff_0
    x_eff_1 = np.linspace(0.8, 2.2, 140)
    y_eff_1 = x_eff_1 * (x_eff_1 + 0.2) ** 2

    x_eff = np.concatenate((x_eff_0, x_eff_1))
    y_eff = np.concatenate((y_eff_0, y_eff_1))

    return (x_perf, y_perf, x_eff, y_eff)

x, y = optimal()
x_perf, y_perf, x_eff, y_eff = original()

plt.figure(figsize=(16, 9))

plt.plot(x_perf, y_perf, label="$Power_{perf}(Perf)$", linewidth=4, linestyle='--', color='blue')
plt.plot(x_eff, y_eff, label="$Power_{eff}(Perf)$", linewidth=4, linestyle='--', color='orange')

plt.plot(x, y, label="$Power_{opt}(Perf)$", linewidth=3, color='black')

plt.xlabel("Perf", fontsize=16)
plt.ylabel("Power", fontsize=16)
plt.title("Power(Perf)", fontsize=24)
plt.legend(fontsize=16)
plt.grid(True)

plt.savefig("image.png")

plt.show()
