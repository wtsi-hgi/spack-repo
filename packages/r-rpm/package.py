# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpm(RPackage):
	"""Modeling of Revealed Preferences Matchings

	Statistical estimation of revealed preference models from data collected on bipartite matchings. The models are for matchings within a bipartite population where individuals have utility for people based on known and unknown characteristics. People can form a partnership or remain unpartnered. The model represents both the availability of potential partners of different types and preferences of individuals for such people. The software estimates preference parameters based on sample survey data on partnerships and population composition. The simulation of matchings and goodness-of-fit are considered.  See Goyal, Handcock, Jackson, Rendall and Yeung (2022) <doi:10.1093/jrsssa/qnad031>.
	"""
	
	homepage = "https://github.com/handcock/rpm"
	cran = "rpm" 

	version("0.7-1", md5="505c7e332a0459845c312644e26bb972")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
