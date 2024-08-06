# Source: https://zenodo.org/records/10829757
import os
from rocrate.rocrate import ROCrate

path_to_metadata = "metadata/"

crate = ROCrate()
i = 0
for subdir in os.listdir(path_to_metadata):
    crate.add_dataset(path_to_metadata + subdir)
    crate.write("roCrates/test_crate" + str(i))
    i += 1
    crate = ROCrate()
# metadata = crate.add_file("../metadata-tsv/Q1101.tsv", properties={
#     "name": "dataset metadata",
#     "encodingFormat": "text/tab-separated-values"
# })


