# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFci(RPackage):
    """f-divergence Cutoff Index for Differential Expression Analysis in Transcriptomics and Proteomics

    (f-divergence Cutoff Index), is to find DEGs in the transcriptomic & proteomic data, and identify DEGs by computing the difference between the distribution of fold-changes for the control-control and remaining (non-differential) case-control gene expression ratio data. fCI provides several advantages compared to existing methods.
    """

    bioc = "fCI"

    version("1.38.0", commit="8f862e6c2d82ae9bb42ff526f7d2a46e758cdd4b")
    version("1.32.0", commit="28433e715e1f5f5a1de04d585215b524f1c6e754")

    depends_on("r@3.1:", type=("build", "run"))
    depends_on("r-fnn", type=("build", "run"))
    depends_on("r-psych", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-zoo", type=("build", "run"))
    depends_on("r-rgl", type=("build", "run"))
    depends_on("r-venndiagram", type=("build", "run"))
