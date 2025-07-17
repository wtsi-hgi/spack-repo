# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimecourse(RPackage):
    """Statistical Analysis for Developmental Microarray Time Course Data

    Functions for data analysis and graphical displays for developmental microarray time course data.
    """

    homepage = "http://www.bioconductor.org"
    bioc = "timecourse"

    version("1.80.0", commit="c971c744f53ccfd5eb0a1c42e92f185a8bcefdb1")
    version("1.74.0", commit="cf915a91adaba40d15d604bc32eac906d37fd632")

    depends_on("r@2.1.1:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-limma@1.8.6:", type=("build", "run"))
    depends_on("r-marray", type=("build", "run"))
