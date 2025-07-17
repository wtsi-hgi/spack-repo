# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKebabs(RPackage):
    """Kernel-Based Analysis Of Biological Sequences

    The package provides functionality for kernel-based analysis of DNA, RNA, and amino acid sequences via SVM-based methods. As core functionality, kebabs implements following sequence kernels: spectrum kernel, mismatch kernel, gappy pair kernel, and motif kernel. Apart from an efficient implementation of standard position-independent functionality, the kernels are extended in a novel way to take the position of patterns into account for the similarity measure. Because of the flexibility of the kernel formulation, other kernels like the weighted degree kernel or the shifted weighted degree kernel with constant weighting of positions are included as special cases. An annotation-specific variant of the kernels uses annotation information placed along the sequence together with the patterns in the sequence. The package allows for the generation of a kernel matrix or an explicit feature representation in dense or sparse format for all available kernels which can be used with methods implemented in other R packages. With focus on SVM-based methods, kebabs provides a framework which simplifies the usage of existing SVM implementations in kernlab, e1071, and LiblineaR. Binary and multi-class classification as well as regression tasks can be used in a unified way without having to deal with the different functions, parameters, and formats of the selected SVM. As support for choosing hyperparameters, the package provides cross validation - including grouped cross validation, grid search and model selection functions. For easier biological interpretation of the results, the package computes feature weights for all SVMs and prediction profiles which show the contribution of individual sequence positions to the prediction result and indicate the relevance of sequence sections for the learning result and the underlying biological functions.
    """

    homepage = "http://www.bioinf.jku.at/software/kebabs/"
    bioc = "kebabs"

    version("1.42.0", commit="b65d0fb0597ae1e5795506bc5fdf5c5b457d2f0b")
    version("1.36.0", commit="79c8b1b1e8940aaead24c5711ad9d2da34167f56")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-kernlab", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-matrix@1.5.0:", type=("build", "run"))
    depends_on("r-xvector", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-liblinear", type=("build", "run"))
    depends_on("r-apcluster", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
