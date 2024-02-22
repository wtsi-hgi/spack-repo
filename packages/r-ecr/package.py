# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcr(RPackage):
	"""Evolutionary Computation in R

	Framework for building evolutionary algorithms for both single- and multi-objective continuous or discrete optimization problems. A set of predefined evolutionary building blocks and operators is included. Moreover, the user can easily set up custom objective functions, operators, building blocks and representations sticking to few conventions. The package allows both a black-box approach for standard tasks (plug-and-play style) and a much more flexible white-box approach where the evolutionary cycle is written by hand.
	"""
	
	homepage = "https://github.com/jakobbossek/ecr2"
	cran = "ecr" 

	version("2.1.1", md5="526e4bdf8406660f01dcaeb859511185")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bbmisc@1.6:", type=("build", "run"))
	depends_on("r-smoof@1.4:", type=("build", "run"))
	depends_on("r-paramhelpers@1.1:", type=("build", "run"))
	depends_on("r-checkmate@1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-parallelmap@1.3:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-plot3drgl", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
