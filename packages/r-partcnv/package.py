# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartcnv(RPackage):
    """Infer locally aneuploid cells using single cell RNA-seq data

    This package uses a statistical framework for rapid and accurate detection of aneuploid cells with local copy number deletion or amplification. Our method uses an EM algorithm with mixtures of Poisson distributions while incorporating cytogenetics information (e.g., regional deletion or amplification) to guide the classification (partCNV). When applicable, we further improve the accuracy by integrating a Hidden Markov Model for feature selection (partCNVH).
    """

    bioc = "partCNV"

    version("1.6.0", commit="6d45f26189a92520ea1c2d77424263a87fc2b4a8")
    version("1.0.0", commit="4075147c471b72fdf0f6c3c7b716e1773d5d82de")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-depmixs4", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
