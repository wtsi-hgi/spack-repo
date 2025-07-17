# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplicinggraphs(RPackage):
    """Create, manipulate, visualize splicing graphs, and assign RNA-seq reads to them

    This package allows the user to create, manipulate, and visualize splicing graphs and their bubbles based on a gene model for a given organism. Additionally it allows the user to assign RNA-seq reads to the edges of a set of splicing graphs, and to summarize them in different ways.
    """

    homepage = "https://bioconductor.org/packages/SplicingGraphs"
    bioc = "SplicingGraphs"

    version("1.48.0", commit="49da9323d872aa3b24971afa8ce7a51c8cc48582")
    version("1.42.0", commit="ed0e2f68d9ba026e75b524550277a181f4b4b141")

    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors@0.17.5:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-iranges@2.21.2:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges@1.23.21:", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
