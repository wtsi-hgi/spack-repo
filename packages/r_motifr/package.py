# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotifr(RPackage):
	"""Motif Analysis in Multi-Level Networks

	Tools for motif analysis in multi-level networks.
    Multi-level networks combine multiple networks in one, e.g.
    social-ecological networks. Motifs are small configurations of nodes
    and edges (subgraphs) occurring in networks. 'motifr' can visualize
    multi-level networks, count multi-level network motifs and compare
    motif occurrences to baseline models. It also identifies contributions
    of existing or potential edges to motifs to find critical or missing
    edges. The package is in many parts an R wrapper for the excellent
    'SESMotifAnalyser' 'Python' package written by Tim Seppelt.
	"""
	
	homepage = "https://marioangst.github.io/motifr/"
	cran = "motifr" 

	version("1.0.0", md5="7a44db8a7714890d9e0c8b167d31e173")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("python@3:", type=("build", "link", "run"))
	depends_on("py-numpy", type=("build", "link", "run"))
	depends_on("py-pandas", type=("build", "link", "run"))
