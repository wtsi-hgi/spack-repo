# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScde(RPackage):
    """Single Cell Differential Expression

    The scde package implements a set of statistical methods for analyzing single-cell RNA-seq data. scde fits individual error models for single-cell RNA-seq measurements. These models can then be used for assessment of differential expression between groups of cells, as well as other types of analysis. The scde package also contains the pagoda framework which applies pathway and gene set overdispersion analysis to identify and characterize putative cell subpopulations based on transcriptional signatures. The overall approach to the differential expression analysis is detailed in the following publication: "Bayesian approach to single-cell differential expression analysis" (Kharchenko PV, Silberstein L, Scadden DT, Nature Methods, doi: 10.1038/nmeth.2967). The overall approach to subpopulation identification and characterization is detailed in the following pre-print: "Characterizing transcriptional heterogeneity through pathway and gene set overdispersion analysis" (Fan J, Salathia N, Liu R, Kaeser G, Yung Y, Herman J, Kaper F, Fan JB, Zhang K, Chun J, and Kharchenko PV, Nature Methods, doi:10.1038/nmeth.3734).
    """

    homepage = "http://pklab.med.harvard.edu/scde"
    bioc = "scde"

    version("2.36.0", commit="7cdd70a855f49813026ddcd5f06ab32e101d5e99")
    version("2.30.0", commit="4a9f09221a914de8ed2796e2dd1c6b8bab2ca350")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-flexmix", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
    depends_on("r-rook", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-cairo", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-quantreg", type=("build", "run"))
    depends_on("r-nnet", type=("build", "run"))
    depends_on("r-rmtstat", type=("build", "run"))
    depends_on("r-extremes", type=("build", "run"))
    depends_on("r-pcamethods", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
