# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbcbook1(RPackage):
    """Support for Springer monograph on Bioconductor

    tools for building book
    """

    homepage = "http://www.biostat.harvard.edu/~carey"
    bioc = "RbcBook1"

    version("1.76.0", commit="5c9602a73fe5a5e580a228a37c50ffadef5ca4de")
    version("1.70.0", commit="751f424a522021bd1c2cbab2520ab2c225363024")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rpart", type=("build", "run"))
