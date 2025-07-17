# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFusesom(RPackage):
    """A Correlation Based Multiview Self Organizing Maps Clustering For IMC Datasets

    A correlation-based multiview self-organizing map for the characterization of cell types in highly multiplexed in situ imaging cytometry assays (`FuseSOM`) is a tool for unsupervised clustering. `FuseSOM` is robust and achieves high accuracy by combining a `Self Organizing Map` architecture and a `Multiview` integration of correlation based metrics. This allows FuseSOM to cluster highly multiplexed in situ imaging cytometry assays.
    """

    bioc = "FuseSOM"

    version("1.10.0", commit="af1bc7dcf691e30b5db775930f69518ebea84af3")
    version("1.4.0", commit="ab1cc4146cd6119d221297bfa68a79d9f224241f")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-psych", type=("build", "run"))
    depends_on("r-fcps", type=("build", "run"))
    depends_on("r-analogue", type=("build", "run"))
    depends_on("r-coop", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-ggplotify", type=("build", "run"))
    depends_on("r-fastcluster", type=("build", "run"))
    depends_on("r-fpc", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-proxy", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-diptest", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
