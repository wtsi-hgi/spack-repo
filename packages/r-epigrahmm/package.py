# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpigrahmm(RPackage):
    """Epigenomic R-based analysis with hidden Markov models

    epigraHMM provides a set of tools for the analysis of epigenomic data based on hidden Markov Models. It contains two separate peak callers, one for consensus peaks from biological or technical replicates, and one for differential peaks from multi-replicate multi-condition experiments. In differential peak calling, epigraHMM provides window-specific posterior probabilities associated with every possible combinatorial pattern of read enrichment across conditions.
    """

    bioc = "epigraHMM"

    version("1.16.0", commit="dfdf56304c08cf2427cb0d3d20c4b1ef45a86b43")
    version("1.10.0", commit="810c6f90776e0128adb53996fb55ca11560a2d78")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-bamsignals", type=("build", "run"))
    depends_on("r-csaw", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-rhdf5lib", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-greylistchip", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
