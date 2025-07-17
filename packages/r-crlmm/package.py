# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrlmm(RPackage):
    """Genotype Calling (CRLMM) and Copy Number Analysis tool for Affymetrix SNP 5.0 and 6.0 and Illumina arrays

    Faster implementation of CRLMM specific to SNP 5.0 and 6.0 arrays, as well as a copy number tool specific to 5.0, 6.0, and Illumina platforms.
    """

    bioc = "crlmm"

    version("1.66.0", commit="8a814b7baa34ca8d344722f8b844f140f4d9cc2b")
    version("1.60.0", commit="1271399d1337a66d46a94469f407a612c15c5d6e")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-oligoclasses@1.21.12:", type=("build", "run"))
    depends_on("r-preprocesscore@1.17.7:", type=("build", "run"))
    depends_on("r-biobase@2.15.4:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-affyio@1.23.2:", type=("build", "run"))
    depends_on("r-illuminaio", type=("build", "run"))
    depends_on("r-ellipse", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-ff", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-rcppeigen@0.3.1.2.1:", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-vgam", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-beanplot", type=("build", "run"))
