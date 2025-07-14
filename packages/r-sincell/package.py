# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSincell(RPackage):
	"""R package for the statistical assessment of cell state hierarchies from single-cell RNA-seq data

	Cell differentiation processes are achieved through a continuum of hierarchical intermediate cell-states that might be captured by single-cell RNA seq. Existing computational approaches for the assessment of cell-state hierarchies from single-cell data might be formalized under a general workflow composed of i) a metric to assess cell-to-cell similarities (combined or not with a dimensionality reduction step), and ii) a graph-building algorithm (optionally making use of a cells-clustering step). Sincell R package implements a methodological toolbox allowing flexible workflows under such framework. Furthermore, Sincell contributes new algorithms to provide cell-state hierarchies with statistical support while accounting for stochastic factors in single-cell RNA seq. Graphical representations and functional association tests are provided to interpret hierarchies.
	"""
	
	homepage = "http://bioconductor.org/"
	bioc = "sincell" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sincell_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sincell/sincell_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="460c0fdd8f97dd266bac81b80af04f8605c14290cd939db90a7f242d3bd3a02a")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-fastica", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
