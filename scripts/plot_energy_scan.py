import numpy as np
import matplotlib.pyplot as plt

# fake distance
r = np.linspace(1.5, 5.0, 50)

# synthetic energy (just for demo)
E = -1 / r + 0.05 * r

plt.figure()
plt.plot(r, E)
plt.xlabel("Distance (Å)")
plt.ylabel("Energy (arb. units)")
plt.title("Synthetic Adsorption Energy Scan")
plt.grid()

plt.savefig("figures/energy_scan.png", dpi=300)
plt.show()
