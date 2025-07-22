# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdbasedufe(RPackage):
    """Tensor Decomposition Based Unsupervised Feature Extraction

    This is a comprehensive package to perform Tensor decomposition based unsupervised feature extraction. It can perform unsupervised feature extraction. It uses tensor decomposition. It is applicable to gene expression, DNA methylation, and histone modification etc. It can perform multiomics analysis. It is also potentially applicable to single cell omics data sets.
    """

    homepage = "https://github.com/tagtag/TDbasedUFE"
    bioc = "TDbasedUFE"

    version("1.8.0", commit="018bf377247ad106894ea8cc358a4b886c706e22")
    version("1.2.0", commit="7f51f6bb5106627d3db30a472d421bf6cf9a1128")

    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rtensor", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-mofadata", type=("build", "run"))
    depends_on("r-tximport", type=("build", "run"))
    depends_on("r-tximportdata", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
