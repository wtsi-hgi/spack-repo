# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosim(RPackage):
    """Multi-Omics Simulation (MOSim)

    MOSim package simulates multi-omic experiments that mimic regulatory mechanisms within the cell, allowing flexible experimental design including time course and multiple groups.
    """

    homepage = "https://github.com/ConesaLab/MOSim"
    bioc = "MOSim"

    version("2.4.0", commit="bd1f062d99c713187122928efca6b490bb6a7441")
    version("1.16.0", commit="4c2e0b98dfe08638bf16d6a5fb2f4d3b441bc1e9")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-hiddenmarkov", type=("build", "run"))
    depends_on("r-zoo", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-lazyeval", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-signac", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
