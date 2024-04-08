# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonocle3(RPackage):
    """SClustering, Differential Expression, and Trajectory Analysis for
    Single-Cell RNA-Seq.

    Monocle 3 performs clustering, differential expression and
    trajectory analysis for single-cell expression experiments. It orders
    individual cells according to progress through a biological process,
    without knowing ahead of time which genes define progress through that
    process. Monocle 3 also performs differential expression analysis,
    clustering, visualization, and other useful tasks on single-cell expression
    data.  It is designed to work with RNA-Seq data, but could be used with
    other types as well."""

    git = "https://github.com/cole-trapnell-lab/monocle3"

    version("1.3.1", tag="v1.3.1")

    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-batchelor", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-future", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrastr", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-grr", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-leidenbase", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-lmtest", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-openssl", type=("build", "run"))
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("r-pbmcapply", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-proxy", type=("build", "run"))
    depends_on("r-pscl", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rann", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rsample", type=("build", "run"))
    depends_on("r-rhpcblasctl", type=("build", "run"))
    depends_on("r-rcppannoy", type=("build", "run"))
    depends_on("r-rcpphnsw", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-slam", type=("build", "run"))
    depends_on("r-spdep", type=("build", "run"))
    depends_on("r-speedglm", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-uwot", type=("build", "run"))
    depends_on("r-terra", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run")
