# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirtarrnaseq(RPackage):
    """mirTarRnaSeq

    mirTarRnaSeq R package can be used for interactive mRNA miRNA sequencing statistical analysis. This package utilizes expression or differential expression mRNA and miRNA sequencing results and performs interactive correlation and various GLMs (Regular GLM, Multivariate GLM, and Interaction GLMs ) analysis between mRNA and miRNA expriments. These experiments can be time point experiments, and or condition expriments.
    """

    bioc = "mirTarRnaSeq"

    version("1.16.0", commit="560893be73c6eb2260b60bb295cdb53e684d6ed6")
    version("1.10.0", commit="582cbaaa192128900f26bd6be287926165ddc4ae")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-pscl", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-catools", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-corrplot", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
