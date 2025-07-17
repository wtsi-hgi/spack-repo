# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRetrofit(RPackage):
    """RETROFIT: Reference-free deconvolution of cell mixtures in spatial transcriptomics

    RETROFIT is a Bayesian non-negative matrix factorization framework to decompose cell type mixtures in ST data without using external single-cell expression references. RETROFIT outperforms existing reference-based methods in estimating cell type proportions and reconstructing gene expressions in simulations with varying spot size and sample heterogeneity, irrespective of the quality or availability of the single-cell reference. RETROFIT recapitulates known cell-type localization patterns in a Slide-seq dataset of mouse cerebellum without using any single-cell data.
    """

    homepage = "https://github.com/qunhualilab/retrofit"
    bioc = "retrofit"

    version("1.8.0", commit="906eef6fbef821cb2b1cc365367644792a1ad1ca")
    version("1.2.0", commit="4e64c2f48688f56de64a32a674a7d4c62323c467")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
