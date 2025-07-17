# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REegc(RPackage):
    """Engineering Evaluation by Gene Categorization (eegc)

    This package has been developed to evaluate cellular engineering processes for direct differentiation of stem cells or conversion (transdifferentiation) of somatic cells to primary cells based on high throughput gene expression data screened either by DNA microarray or RNA sequencing. The package takes gene expression profiles as inputs from three types of samples: (i) somatic or stem cells to be (trans)differentiated (input of the engineering process), (ii) induced cells to be evaluated (output of the engineering process) and (iii) target primary cells (reference for the output). The package performs differential gene expression analysis for each pair-wise sample comparison to identify and evaluate the transcriptional differences among the 3 types of samples (input, output, reference). The ideal goal is to have induced and primary reference cell showing overlapping profiles, both very different from the original cells.
    """

    bioc = "eegc"

    version("1.28.0", commit="5fcfa134486762ef2afbd150d318a31cb8503ed4")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-sna", type=("build", "run"))
    depends_on("r-wordcloud", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-clusterprofiler", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-org-mm-eg-db", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-dose", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
