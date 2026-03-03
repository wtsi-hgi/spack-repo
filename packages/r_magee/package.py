# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagee(RPackage):
    """Mixed Model Association Test for GEne-Environment Interaction

    Use a 'glmmkin' class object (GMMAT package) from the null model to perform generalized linear mixed model-based single-variant and variant set main effect tests, gene-environment interaction tests, and joint tests for association, as proposed in Wang et al. (2020) <DOI:10.1002/gepi.22351>.
    """

    cran = "MAGEE"

    version("1.4.1", sha256="fa5c4521d9bb034b90ed3407a0c49f562ddfa00352a9ed84a9b90b21e45e6a76")
    version("1.3.2", md5="29eb11b0e7f407c790b29815145b1d6d")
    version("1.3.0", md5="3f259300e90127c692ecd70cbb2d7076")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-gmmat", type=("build", "run"))
    depends_on("r-compquadform", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-seqarray", type=("build", "run"))
    depends_on("r-seqvartools", type=("build", "run"))
    depends_on("bzip2", type=("build", "link", "run"))
    depends_on("zlib", type=("build", "link", "run"))
    depends_on("zstd", type=("build", "link", "run"))
    depends_on("libdeflate", type=("build", "link", "run"))
