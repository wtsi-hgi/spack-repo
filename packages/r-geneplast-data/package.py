# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneplastData(RPackage):
    """Input data for the geneplast package via AnnotationHub

    The package geneplast.data provides datasets from different sources via AnnotationHub to use in geneplast pipelines. The datasets have species, phylogenetic trees, and orthology relationships among eukaryotes from different orthologs databases.
    """

    bioc = "geneplast.data"

    version("0.99.9", commit="847b6b266d262c322d1a85ee6708001de01946b0")
    version("0.99.9", commit="847b6b266d262c322d1a85ee6708001de01946b0")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-treeio", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-geneplast", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
