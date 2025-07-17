# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigmelon(RPackage):
    """Illumina methylation array analysis for large experiments

    Methods for working with Illumina arrays using gdsfmt.
    """

    bioc = "bigmelon"

    version("1.34.0", commit="45e85af06cbadcc79e1dba106a14ae3dfc326cf9")
    version("1.28.0", commit="80fe6d4d6a5513d0b6c3639eaa31084dde46d43b")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-watermelon@1.25:", type=("build", "run"))
    depends_on("r-gdsfmt@1.0.4:", type=("build", "run"))
    depends_on("r-minfi@1.21:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-methylumi", type=("build", "run"))
    depends_on("r-geoquery", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-illuminaio", type=("build", "run"))
