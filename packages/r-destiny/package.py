# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDestiny(RPackage):
    """Creates diffusion maps

    Create and plot diffusion maps.
    """

    homepage = "https://theislab.github.io/destiny/"
    bioc = "destiny"

    version("3.22.0", commit="7bfea59ab5aba3db1a710b5176934f24669c4f3c")
    version("3.16.0", commit="300eb293fb773fb3d667818b946fdd3c62b0aa05")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-rspectra@0.14.0:", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-pcamethods", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggplot-multistats", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
    depends_on("r-ggthemes", type=("build", "run"))
    depends_on("r-vim", type=("build", "run"))
    depends_on("r-knn-covertree", type=("build", "run"))
    depends_on("r-proxy", type=("build", "run"))
    depends_on("r-rcpphnsw", type=("build", "run"))
    depends_on("r-smoother", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-scatterplot3d", type=("build", "run"))
