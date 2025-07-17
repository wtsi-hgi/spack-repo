# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDune(RPackage):
    """Improving replicability in single-cell RNA-Seq cell type discovery

    Given a set of clustering labels, Dune merges pairs of clusters to increase mean ARI between labels, improving replicability.
    """

    bioc = "Dune"

    version("1.20.0", commit="f38fdd92221e0a397d2718572a15cf038a79dabd")
    version("1.14.0", commit="b34c4dbc2d97d11877062bc872565a0fb91aeff5")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-gganimate", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-aricode", type=("build", "run"))
