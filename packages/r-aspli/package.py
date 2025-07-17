# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAspli(RPackage):
    """Analysis of Alternative Splicing Using RNA-Seq

    Integrative pipeline for the analysis of alternative splicing using RNAseq.
    """

    bioc = "ASpli"

    version("2.18.0", commit="8646ccc554727478af6552f892ceca6807a4e22b")
    version("2.12.0", commit="bf94d057deaae124c225ef308543b6844e1175b3")

    depends_on("r-edger", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-upsetr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-pbmcapply", type=("build", "run"))
