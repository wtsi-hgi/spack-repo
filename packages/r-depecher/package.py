# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepecher(RPackage):
    """Determination of essential phenotypic elements of clusters in high-dimensional entities

    The purpose of this package is to identify traits in a dataset that can separate groups. This is done on two levels. First, clustering is performed, using an implementation of sparse K-means. Secondly, the generated clusters are used to predict outcomes of groups of individuals based on their distribution of observations in the different clusters. As certain clusters with separating information will be identified, and these clusters are defined by a sparse number of variables, this method can reduce the complexity of data, to only emphasize the data that actually matters.
    """

    bioc = "DepecheR"

    version("1.24.0", commit="b4010877830b9da9723606ce67bcb6758f922463")
    version("1.18.0", commit="14db2295189951d35cf83d4b2f474651580c31b6")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-ggplot2@3.1:", type=("build", "run"))
    depends_on("r-mass@7.3.51:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-dplyr@0.7.8:", type=("build", "run"))
    depends_on("r-gplots@3.0.1:", type=("build", "run"))
    depends_on("r-viridis@0.5.1:", type=("build", "run"))
    depends_on("r-foreach@1.4.4:", type=("build", "run"))
    depends_on("r-dosnow@1.0.16:", type=("build", "run"))
    depends_on("r-matrixstats@0.54:", type=("build", "run"))
    depends_on("r-mixomics@6.6.1:", type=("build", "run"))
    depends_on("r-moments@0.14:", type=("build", "run"))
    depends_on("r-reshape2@1.4.3:", type=("build", "run"))
    depends_on("r-beanplot@1.2:", type=("build", "run"))
    depends_on("r-fnn@1.1.3:", type=("build", "run"))
    depends_on("r-robustbase@0.93.5:", type=("build", "run"))
    depends_on("r-gmodels@2.18.1:", type=("build", "run"))
    depends_on("r-collapse@1.9.2:", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
