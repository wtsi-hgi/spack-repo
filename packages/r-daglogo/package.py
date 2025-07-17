# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaglogo(RPackage):
    """dagLogo: a Bioconductor package for visualizing conserved amino acid sequence pattern in groups based on probability theory

    Visualize significant conserved amino acid sequence pattern in groups based on probability theory.
    """

    bioc = "dagLogo"

    version("1.46.0", commit="c43e8c31056316e32a46792642b721e1879d2228")
    version("1.40.0", commit="5fd07790c2f8bb9783767bb080be4e9c65c2550a")

    depends_on("r@3.0.1:", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-uniprot-ws", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-motifstack", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
