# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgraph(RPackage):
	"""Graph Plotting Methods, Psychometric Data Visualization and
Graphical Model Estimation

	Fork of qgraph - Weighted network visualization and analysis, as well as Gaussian graphical model computation. See Epskamp et al. (2012) <doi:10.18637/jss.v048.i04>.
	"""
	
	cran = "qgraph" 

	version("1.9.8", md5="9bae87f6517136bc0d7e2be98406a3bc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
