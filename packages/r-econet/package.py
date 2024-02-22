# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REconet(RPackage):
	"""Estimation of Parameter-Dependent Network Centrality Measures

	Provides methods for estimating parameter-dependent network centrality measures with linear-in-means models. Both non linear least squares and maximum likelihood estimators are implemented. The methods allow for both link and node heterogeneity in network effects, endogenous network formation and the presence of unconnected nodes. The routines also compare the explanatory power of parameter-dependent network centrality measures with those of standard measures of network centrality. Benefits and features of the 'econet' package are illustrated using data from Battaglini and Patacchini (2018) and Battaglini, Patacchini, and Leone Sciabolazza (2020). For additional details, see the vignette <doi:10.18637/jss.v102.i08>.
	"""
	
	cran = "econet" 

	version("1.0.0", md5="f4fa691733cd705c810e03054d37b412")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
