# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondiments(RPackage):
    """Differential Topology, Progression and Differentiation

    This package encapsulate many functions to conduct a differential topology analysis. It focuses on analyzing an 'omic dataset with multiple conditions. While the package is mostly geared toward scRNASeq, it does not place any restriction on the actual input format.
    """

    homepage = "https://hectorrdb.github.io/condiments/index.html"
    bioc = "condiments"

    version("1.16.0", commit="7cbdad44cb2ec4da6d71c8960256cb49a195fc66")
    version("1.10.0", commit="d7f032b005bd7dfcb374b411667c9f624b9972ae")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-slingshot@1.9:", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
    depends_on("r-rann", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-dplyr@1:", type=("build", "run"))
    depends_on("r-ecume@0.9.1:", type=("build", "run"))
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-trajectoryutils", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-distinct", type=("build", "run"))
