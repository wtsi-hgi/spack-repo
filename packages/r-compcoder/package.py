# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompcoder(RPackage):
    """RNAseq data simulation, differential expression analysis and performance comparison of differential expression methods

    This package provides extensive functionality for comparing results obtained by different methods for differential expression analysis of RNAseq data. It also contains functions for simulating count data. Finally, it provides convenient interfaces to several packages for performing the differential expression analysis. These can also be used as templates for setting up and running a user-defined differential analysis workflow within the framework of the package.
    """

    homepage = "https://github.com/csoneson/compcodeR"
    bioc = "compcodeR"

    version("1.44.0", commit="540101d48efacf75b6b60fa17274d9b5c26aa92e")
    version("1.38.0", commit="1bea8af3f2b5c557125facf8a4706be8e80e939d")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-sm", type=("build", "run"))
    depends_on("r-knitr@1.2:", type=("build", "run"))
    depends_on("r-markdown", type=("build", "run"))
    depends_on("r-rocr", type=("build", "run"))
    depends_on("r-lattice@0.16:", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-catools", type=("build", "run"))
    depends_on("r-kernsmooth", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-modeest", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-vioplot", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-phylolm", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinydashboard", type=("build", "run"))
