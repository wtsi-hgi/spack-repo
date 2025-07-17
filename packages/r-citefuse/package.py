# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitefuse(RPackage):
    """CiteFuse: multi-modal analysis of CITE-seq data

    CiteFuse pacakage implements a suite of methods and tools for CITE-seq data from pre-processing to integrative analytics, including doublet detection, network-based modality integration, cell type clustering, differential RNA and protein expression analysis, ADT evaluation, ligand-receptor interaction analysis, and interactive web-based visualisation of the analyses.
    """

    bioc = "CiteFuse"

    version("1.20.0", commit="051ba244d75a1f2741b82091b1d54d35349815b5")
    version("1.14.0", commit="154770ff14d2aeac044563e32b072946e1899dcc")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-singlecellexperiment@1.8:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.16:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mixtools", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-dbscan", type=("build", "run"))
    depends_on("r-uwot", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-s4vectors@0.24:", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-scran@1.14.6:", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggridges", type=("build", "run"))
    depends_on("r-randomforest", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-compositions", type=("build", "run"))
