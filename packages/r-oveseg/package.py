# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROveseg(RPackage):
    """OVESEG-test to detect tissue/cell-specific markers

    An R package for multiple-group comparison to detect tissue/cell-specific marker genes among subtypes. It provides functions to compute OVESEG-test statistics, derive component weights in the mixture null distribution model and estimate p-values from weightedly aggregated permutations. Obtained posterior probabilities of component null hypotheses can also portrait all kinds of upregulation patterns among subtypes.
    """

    bioc = "OVESEG"

    version("1.24.0", commit="47353d509f876e6db67900e41a4a80964c32fdfb")
    version("1.18.0", commit="f01b152f94598306f0a869b5b9b4db26a2690361")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-fdrtool", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
