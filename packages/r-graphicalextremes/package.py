# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphicalextremes(RPackage):
	"""Statistical Methodology for Graphical Extreme Value Models

	Statistical methodology for sparse multivariate extreme value models. Methods are
             provided for exact simulation and statistical inference for multivariate Pareto distributions
             on graphical structures as described in the paper 'Graphical Models for Extremes' by
             Engelke and Hitz (2020) <doi:10.1111/rssb.12355>. 
	"""
	
	homepage = "https://github.com/sebastian-engelke/graphicalExtremes"
	cran = "graphicalExtremes" 

	version("0.3.1", md5="727bc03208bbfaf8bd81f7473e2e4717")
	version("0.3.0", md5="f19d997895f7dbc8be65479a56bf8678")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph@1.2.4.1:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.10:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-glassofast", type=("build", "run"))
	depends_on("r-edmcr", type=("build", "run"))
