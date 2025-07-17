# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsica(RPackage):
    """consensus Independent Component Analysis

    consICA implements a data-driven deconvolution method – consensus independent component analysis (ICA) to decompose heterogeneous omics data and extract features suitable for patient diagnostics and prognostics. The method separates biologically relevant transcriptional signals from technical effects and provides information about the cellular composition and biological processes. The implementation of parallel computing in the package ensures efficient analysis of modern multicore systems.
    """

    bioc = "consICA"

    version("2.6.0", commit="97d984a90823de13d3344f73845ca63857a6fa0e")
    version("2.0.0", commit="d7fa01ed04549e6ea695fa1c0e109fedc8c0f2a3")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-fastica@1.2.1:", type=("build", "run"))
    depends_on("r-sm", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rfast", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-topgo", type=("build", "run"))
