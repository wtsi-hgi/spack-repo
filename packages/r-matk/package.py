# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatk(RPackage):
    """Visualize metacells and evaluate their quality."""

    homepage = "https://github.com/GfellerLab/MetacellAnalysisToolkit"
    git = "https://github.com/GfellerLab/MetacellAnalysisToolkit.git"

    version("20240808", commit="bc3c67af52a121291eab5e8a02c30d55017a8d95")

    depends_on("r@4.0:", type=("build", "run"))
    depends_on("r-anndata", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-sparsematrixstats", type=("build", "run"))
    depends_on("r-supercell", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
