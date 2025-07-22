# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmelsgi(RPackage):
    """Experimental data and documented source code for the paper "A Map of Directional Genetic Interactions in a Metazoan Cell"

    The package contains the experimental data and documented source code of the manuscript "Fischer et al., A Map of Directional Genetic Interactions in a Metazoan Cell, eLife, 2015, in Press.". The vignette code generates all figures in the paper.
    """

    bioc = "DmelSGI"

    version("1.34.0", commit="af5e733f506eb11991dc580d40867f27a6d39df5")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-tsp", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
