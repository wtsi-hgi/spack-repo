# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarmony2(RPackage):
    """Fast, sensitive, and accurate integration of single-cell data.

    Harmony2 implements the next-generation Harmony algorithm together with
    interfaces for popular single-cell workflows.
    """

    homepage = "https://github.com/immunogenomics/harmony"
    git = "https://github.com/immunogenomics/harmony.git"

    license("GPL-3.0-or-later")

    version("2.0.1", commit="83f3e8a68391d9a7374142e43656f4e034cc9d3e")

    depends_on("r@4.2.0:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-rcpp")
        depends_on("r-rcpparmadillo")
        depends_on("r-rcppprogress")
        depends_on("r-dplyr")
        depends_on("r-cowplot")
        depends_on("r-ggplot2")
        depends_on("r-matrix")
        depends_on("r-tibble")
        depends_on("r-rlang")
        depends_on("r-rhpcblasctl")
        depends_on("r-cli")
