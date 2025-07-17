# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylmix(RPackage):
    """MethylMix: Identifying methylation driven cancer genes

    MethylMix is an algorithm implemented to identify hyper and hypomethylated genes for a disease. MethylMix is based on a beta mixture model to identify methylation states and compares them with the normal DNA methylation state. MethylMix uses a novel statistic, the Differential Methylation value or DM-value defined as the difference of a methylation state with the normal methylation state. Finally, matched gene expression data is used to identify, besides differential, functional methylation states by focusing on methylation changes that effect gene expression. References: Gevaert 0. MethylMix: an R package for identifying DNA methylation-driven genes. Bioinformatics (Oxford, England). 2015;31(11):1839-41. doi:10.1093/bioinformatics/btv020. Gevaert O, Tibshirani R, Plevritis SK. Pancancer analysis of DNA methylation-driven genes using MethylMix. Genome Biology. 2015;16(1):17. doi:10.1186/s13059-014-0579-8.
    """

    bioc = "MethylMix"

    version("2.38.0", commit="fa7c9dc902c5b34a32230b315c03572270a02c6b")
    version("2.32.0", commit="8bb440a41f802f9061a8b580043408e060cbf87d")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-rpmm", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-impute", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-r-matlab", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
