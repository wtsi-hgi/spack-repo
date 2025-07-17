# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcdfflow(RPackage):
    """ncdfFlow: A package that provides HDF5 based storage for flow cytometry data.

    Provides HDF5 storage based methods and functions for manipulation of flow cytometry data.
    """

    bioc = "ncdfFlow"

    version("2.54.0", commit="c78def5d63c2ed22ef7c774760624bc8b10ab68e")
    version("2.48.0", commit="8367dea8a78012d734bc51630ac95a7a73e48ff5")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
    depends_on("r-cpp11", type=("build", "run"))
    depends_on("r-rhdf5lib", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
