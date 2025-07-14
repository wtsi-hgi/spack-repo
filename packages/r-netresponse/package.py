# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetresponse(RPackage):
	"""Functional Network Analysis

	Algorithms for functional network analysis. Includes an implementation of a variational Dirichlet process Gaussian mixture model for nonparametric mixture modeling.
	"""
	
	homepage = "https://github.com/antagomir/netresponse"
	bioc = "netresponse"

	version("1.68.0", commit="6b0d93083d65a39c26cef1c5769c3c5daef76c01")
	version("1.62.0", commit="b3dff344051a071aa99b90f00bd4729eacb9844e")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
