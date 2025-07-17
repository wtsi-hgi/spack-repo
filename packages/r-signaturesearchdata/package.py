# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignaturesearchdata(RPackage):
    """Datasets for signatureSearch package

    CMAP/LINCS hdf5 databases and other annotations used for signatureSearch software package.
    """

    bioc = "signatureSearchData"

    version("1.22.0", commit="79c1dd950973b1c28ca99a1a3260cc0f0d8b0d6d")
    version("1.16.0", commit="71ab882146add47ce103eacfd085540cd9da5225")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
