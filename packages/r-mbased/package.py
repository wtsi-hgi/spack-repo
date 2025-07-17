# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbased(RPackage):
    """Package containing functions for ASE analysis using Meta-analysis Based Allele-Specific Expression Detection

    The package implements MBASED algorithm for detecting allele-specific gene expression from RNA count data, where allele counts at individual loci (SNVs) are integrated into a gene-specific measure of ASE, and utilizes simulations to appropriately assess the statistical significance of observed ASE.
    """

    bioc = "MBASED"

    version("1.42.0", commit="554cac3ed7c47229a55997ad02e35e89dd31a5a9")
    version("1.36.0", commit="59c9e157f75de8a816c2d5b05d61a08c9b0fa57e")

    depends_on("r-runit", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
