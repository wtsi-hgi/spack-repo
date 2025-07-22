# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH5mread(RPackage):
    """Memory-efficient reading of HDF5 datasets into R.

    The main function in the h5mread package is h5mread(), which allows reading
    arbitrary data from an HDF5 dataset into R, similarly to what the h5read()
    function from the rhdf5 package does. In the case of h5mread(), the
    implementation has been optimized to make it as fast and memory-efficient
    as possible."""

    bioc = "h5mread"
    url = "https://bioconductor.org/packages/release/bioc/src/contrib/h5mread_1.0.1.tar.gz"

    version("1.0.1", sha256="0b63e37635b2934dd42cbe65be34c162")

    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-sparsearray", type=("build", "run"))
    depends_on("r-rhdf5filters", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4arrays", type=("build", "run"))
    depends_on("r-rhdf5lib", type=("build", "link")) 