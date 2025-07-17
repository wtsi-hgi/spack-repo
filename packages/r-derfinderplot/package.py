# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDerfinderplot(RPackage):
    """Plotting functions for derfinder

    This package provides plotting functions for results from the derfinder package. This helps separate the graphical dependencies required for making these plots from the core functionality of derfinder.
    """

    homepage = "https://github.com/leekgroup/derfinderPlot"
    bioc = "derfinderPlot"

    version("1.42.0", commit="dc229b968b32590e29e67edb6b6f6270362b6587")
    version("1.36.0", commit="23673dafb9bbab42e495c7eaa60c902c1d6ad4df")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-derfinder@1.1:", type=("build", "run"))
    depends_on("r-genomeinfodb@1.3.3:", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicranges@1.17.40:", type=("build", "run"))
    depends_on("r-ggbio@1.13.13:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-iranges@1.99.28:", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-s4vectors@0.9.38:", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
