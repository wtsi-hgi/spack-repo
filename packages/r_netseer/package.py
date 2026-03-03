# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetseer(RPackage):
	"""Graph Prediction from a Graph Time Series

	Predicting the structure of a graph including new nodes and edges using
    a time series of graphs. Flux balance analysis, a linear and integer programming 
    technique used in biochemistry is used with time series prediction methods to 
    predict the graph structure at a future time point 
    Kandanaarachchi (2024) <doi:10.48550/arXiv.2401.04280>.
	"""
	
	homepage = "https://sevvandi.github.io/netseer/"
	cran = "netseer" 

	version("0.1.0", md5="4c3de54dbf43e4466ba356f489396d53")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fable", type=("build", "run"))
	depends_on("r-fabletools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
