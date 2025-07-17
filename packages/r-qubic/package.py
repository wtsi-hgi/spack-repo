# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQubic(RPackage):
    """An R package for qualitative biclustering in support of gene co-expression analyses

    The core function of this R package is to provide the implementation of the well-cited and well-reviewed QUBIC algorithm, aiming to deliver an effective and efficient biclustering capability. This package also includes the following related functions: (i) a qualitative representation of the input gene expression data, through a well-designed discretization way considering the underlying data property, which can be directly used in other biclustering programs; (ii) visualization of identified biclusters using heatmap in support of overall expression pattern analysis; (iii) bicluster-based co-expression network elucidation and visualization, where different correlation coefficient scores between a pair of genes are provided; and (iv) a generalize output format of biclusters and corresponding network can be freely downloaded so that a user can easily do following comprehensive functional enrichment analysis (e.g. DAVID) and advanced network visualization (e.g. Cytoscape).
    """

    homepage = "http://github.com/zy26/QUBIC"
    bioc = "QUBIC"

    version("1.36.0", commit="5fe863eeb40683a6ab0dface16fe2d8761276082")
    version("1.30.0", commit="49a174ac93dc585e3e6aebf64b4d36092ec9d574")

    depends_on("r@3.1:", type=("build", "run"))
    depends_on("r-biclust", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
