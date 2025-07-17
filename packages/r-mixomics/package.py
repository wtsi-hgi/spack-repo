# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixomics(RPackage):
    """Omics Data Integration Project

    Multivariate methods are well suited to large omics data sets where the number of variables (e.g. genes, proteins, metabolites) is much larger than the number of samples (patients, cells, mice). They have the appealing properties of reducing the dimension of the data by using instrumental variables (components), which are defined as combinations of all variables. Those components are then used to produce useful graphical outputs that enable better understanding of the relationships and correlation structures between the different data sets that are integrated. mixOmics offers a wide range of multivariate methods for the exploration and integration of biological datasets with a particular focus on variable selection. The package proposes several sparse multivariate models we have developed to identify the key variables that are highly correlated, and/or explain the biological outcome of interest. The data that can be analysed with mixOmics may come from high throughput sequencing technologies, such as omics data (transcriptomics, metabolomics, proteomics, metagenomics etc) but also beyond the realm of omics (e.g. spectral imaging). The methods implemented in mixOmics can also handle missing values without having to delete entire rows with missing data. A non exhaustive list of methods include variants of generalised Canonical Correlation Analysis, sparse Partial Least Squares and sparse Discriminant Analysis. Recently we implemented integrative methods to combine multiple data sets: N-integration with variants of Generalised Canonical Correlation Analysis and P-integration with variants of multi-group Partial Least Squares.
    """

    homepage = "http://www.mixOmics.org"
    bioc = "mixOmics"

    version("6.32.0", commit="36d4efc32957353b63502e67e09051b2bed13be9")
    version("6.26.0", commit="6800c8c59d726593bd6f7966093af8dd6be32dfd")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-ellipse", type=("build", "run"))
    depends_on("r-corpcor", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-rarpack", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
