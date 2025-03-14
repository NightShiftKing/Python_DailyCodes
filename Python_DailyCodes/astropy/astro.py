# work with numbers easier
import numpy as np
# helps draw graphs and pictures
import matplotlib.pyplot as plt
# import fits to open and use special space pciture files
from astropy.io import fits
# to grab data from the internet without leaving code
from astropy.utils.data import download_file
# make space pictures prettier
from astropy.visualization import LogStretch, PowerStretch
# makes our pictures fit on graphs
from astropy.visualization.mpl_normalize import ImageNormalize

image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)
image_file2 = download_file('https://fits.gsfc.nasa.gov/samples/FOCx38i0101t_c0f.fits', cache=True)

image_data = fits.getdata(image_file)
image_data2 = fits.getdata(image_file2)


header = fits.getheader(image_file)
print(header)

print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

plt.figure(figsize=(10,10))
plt.imshow(image_data, cmap='cividis')
plt.colorbar()
plt.show()

plt.imshow(image_data2, cmap='Pastel1')
plt.show()
