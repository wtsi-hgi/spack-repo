# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSupercell(RPackage):
    """SuperCell is an R package for coarse-graining large single-cell RNA-seq data into metacells and performing downstream analysis at the metacell level."""

    homepage = "https://github.com/GfellerLab/SuperCell"
    url = "https://github.com/GfellerLab/SuperCell/archive/refs/tags/v1.0.tar.gz"

    version("1.0", sha256="d24f6bbb3d2c93115579803128411596a3c7780220e89a1f917bf5962858eb52")

    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-rann", type=("build", "run"))
    depends_on("r-weightedcluster", type=("build", "run"))
    depends_on("r-corpcor", type=("build", "run"))
    depends_on("r-weights", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-umap", type=("build", "run"))
    depends_on("r-entropy", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-bluster", type=("build", "run"))
    depends_on("r-dbscan", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-plotfunctions", type=("build", "run"))
    depends_on("r-proxy", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
