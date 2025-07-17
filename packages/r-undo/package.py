# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUndo(RPackage):
    """Unsupervised Deconvolution of Tumor-Stromal Mixed Expressions

    UNDO is an R package for unsupervised deconvolution of tumor and stromal mixed expression data. It detects marker genes and deconvolutes the mixing expression data without any prior knowledge.
    """

    bioc = "UNDO"

    version("1.50.0", commit="9c7de72f524f7a8b1ed2b556cc2f5982fd60ec81")
    version("1.44.0", commit="77b9f60ad951b592dc1c9d4932ef0d374fd51354")

    depends_on("r@2.15.2:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-boot", type=("build", "run"))
    depends_on("r-nnls", type=("build", "run"))
