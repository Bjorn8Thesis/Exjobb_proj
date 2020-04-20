import numpy as np
import h5py

#filename = "concentrations-multires.hdf5"

with h5py.File("/Users/bjoha/OneDrive/Desktop/KTH/Master's Thesis/Data/concentrations-multires.hdf5", "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])
