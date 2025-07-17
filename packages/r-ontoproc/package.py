# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROntoproc(RPackage):
    """processing of ontologies of anatomy, cell lines, and so on

    Support harvesting of diverse bioinformatic ontologies, making particular use of the ontologyIndex package on CRAN. We provide snapshots of key ontologies for terms about cells, cell lines, chemical compounds, and anatomy, to help analyze genome-scale experiments, particularly cell x compound screens. Another purpose is to strengthen development of compelling use cases for richer interfaces to emerging ontologies.
    """

    homepage = "https://github.com/vjcitn/ontoProc"
    bioc = "ontoProc"

    version("2.2.1", commit="3b9f7e222faf4111b91c0e2ffa35869f6895b2cf")
    version("1.24.0", commit="5718db114aea7fd3dadb83e096f87004aa69ddd2")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-ontologyindex", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-ontologyplot", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
