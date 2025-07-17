# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchex(RPackage):
    """Hexbin plots for single cell omics data

    Builds hexbin plots for variables and dimension reduction stored in single cell omics data such as SingleCellExperiment and SeuratObject. The ideas used in this package are based on the excellent work of Dan Carr, Nicholas Lewin-Koh, Martin Maechler and Thomas Lumley.
    """

    homepage = "https://github.com/SaskiaFreytag/schex"
    bioc = "schex"

    version("1.22.0", commit="5ca539aa61e2b0237916a1353fed3014efa99235")
    version("1.16.1", commit="f3bdf546223bd626b9c7b0ab30db9e9db6912101")

    depends_on("r-singlecellexperiment@1.7.4:", type=("build", "run"))
    depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
    depends_on("r-hexbin", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-entropy", type=("build", "run"))
    depends_on("r-ggforce", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-concaveman", type=("build", "run"))
