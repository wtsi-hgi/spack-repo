# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChihaya(RPackage):
    """Save Delayed Operations to a HDF5 File

    Saves the delayed operations of a DelayedArray to a HDF5 file. This enables efficient recovery of the DelayedArray's contents in other languages and analysis frameworks.
    """

    homepage = "https://github.com/ArtifactDB/chihaya-R"
    bioc = "chihaya"

    version("1.8.0", commit="f3454e1ab4e0460d316dc64b1269987a232f1615")
    version("1.2.0", commit="180da647fe1bac5f3a3dfe79d056ebbe526005a5")

    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-rhdf5lib", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
