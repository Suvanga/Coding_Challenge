import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("mouse_velocities.csv")

# Integrate velocity to get position
df["x"] = df["velocity_x"].cumsum()
df["y"] = df["velocity_y"].cumsum()

plt.figure(figsize=(8, 4))
plt.plot(df["x"], -df["y"], linewidth=2)  # invert Y so it looks like screen coordinates
plt.axis("equal")
plt.title("Reconstructed Mouse Path")
plt.show()
