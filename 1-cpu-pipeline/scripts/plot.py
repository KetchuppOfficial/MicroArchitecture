import numpy as np
import matplotlib.pyplot as plt

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

plt.figure(figsize=(16, 9))
plt.plot(x_perf, y_perf, label="$Power_{perf}(Perf)$", linewidth=2, color='blue')
plt.plot(x_eff, y_eff, label="$Power_{eff}(Perf)$", linewidth=2, color='orange')

plt.xlabel("Perf", fontsize=16)
plt.ylabel("Power", fontsize=16)
plt.title("Power(Perf)", fontsize=24)
plt.legend(fontsize=16)
plt.grid(True)

plt.savefig("images/1-1.png")

plt.show()
