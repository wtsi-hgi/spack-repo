# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyntenet(RPackage):
    """Inference And Analysis Of Synteny Networks

    syntenet can be used to infer synteny networks from whole-genome protein sequences and analyze them. Anchor pairs are detected with the MCScanX algorithm, which was ported to this package with the Rcpp framework for R and C++ integration. Anchor pairs from synteny analyses are treated as an undirected unweighted graph (i.e., a synteny network), and users can perform: i. network clustering; ii. phylogenomic profiling (by identifying which species contain which clusters) and; iii. microsynteny-based phylogeny reconstruction with maximum likelihood.
    """

    homepage = "https://github.com/almeidasilvaf/syntenet"
    bioc = "syntenet"

    version("1.10.0", commit="1d459a4195e0c27003e732abf5a12d8b10fdfa53")
    version("1.4.2", commit="4c935258dc265e4e3e022732a0ca4ec764104d8a")
    version("1.4.0", md5="ab56b637f74d79cfba3dd6aab80b7ac9")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggnetwork", type=("build", "run"))
    depends_on("r-intergraph", type=("build", "run"))
    depends_on("r-networkd3", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
