# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDexma(RPackage):
    """Differential Expression Meta-Analysis

    performing all the steps of gene expression meta-analysis considering the possible existence of missing genes. It provides the necessary functions to be able to perform the different methods of gene expression meta-analysis. In addition, it contains functions to apply quality controls, download GEO datasets and show graphical representations of the results.
    """

    bioc = "DExMA"

    version("1.16.0", commit="9d4ff0563ee8123edd16d7d5b5a96dc12ae83e75")
    version("1.10.7", commit="dd6da1e2218e31aa419638983f65fd09644aeb2b")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-dexmadata", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-geoquery", type=("build", "run"))
    depends_on("r-impute", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-snpstats", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-swamp", type=("build", "run"))
    depends_on("r-bnstruct", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
