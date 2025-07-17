# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpistasisga(RPackage):
    """An R package to identify multi-snp effects in nuclear family studies using the GADGETS method

    This package runs the GADGETS method to identify epistatic effects in nuclear family studies. It also provides functions for permutation-based inference and graphical visualization of the results.
    """

    homepage = "https://github.com/mnodzenski/epistasisGA"
    bioc = "epistasisGA"

    version("1.10.0", commit="6b37aae79a9f3ba65384d676881d70eb900a20b2")
    version("1.4.0", commit="a4f5fdc19b42da472d4fd1d163e78c28c69794f5")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-batchtools", type=("build", "run"))
    depends_on("r-qgraph", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-bigmemory", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
