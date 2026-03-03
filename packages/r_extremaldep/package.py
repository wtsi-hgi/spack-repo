# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremaldep(RPackage):
	"""Extremal Dependence Models

	A set of procedures for parametric and non-parametric modelling of the dependence structure of multivariate extreme-values is provided. The statistical inference is performed with non-parametric estimators, likelihood-based estimators and Bayesian techniques. It adapts the methodologies of Beranger and Padoan (2015) <arxiv:1508.05561>, Marcon et al. (2016) <doi:10.1214/16-EJS1162>, Marcon et al. (2017) <doi:10.1002/sta4.145>, Marcon et al. (2017) <doi:10.1016/j.jspi.2016.10.004> and Beranger et al. (2021) <doi:10.1007/s10687-019-00364-0>. This package also allows for the modelling of spatial extremes using flexible max-stable processes. It provides simulation algorithms and fitting procedures relying on the Stephenson-Tawn likelihood as per Beranger at al. (2021) <doi:10.1007/s10687-020-00376-1>.
	"""
	
	homepage = "https://faculty.unibocconi.it/simonepadoan/"
	cran = "ExtremalDep" 

	version("0.0.4-1", md5="a3836e6574e048fd048401b0fc389676")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
