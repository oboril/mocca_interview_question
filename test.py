# Load the chromatogram data
from mocca.dad_data.apis.empower import read_empower
data, time, wavelength = read_empower('sample1.arw')

# Plot a slice of the data
from matplotlib import pyplot as plt
plt.plot(time, data[100])
plt.show()