# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesgmed(RPackage):
	"""Bayesian Causal Mediation Analysis using 'Stan'

	Performs parametric mediation analysis using the Bayesian g-formula approach for binary and continuous outcomes. The methodology is based on Comment (2018) <doi:10.5281/zenodo.1285275> and a demonstration of its application can be found at Yimer et al. (2022) <doi:10.48550/arXiv.2210.08499>. 
	"""
	
	cran = "BayesGmed" 

	version("0.0.3", md5="3fce8dbeda67f1d2f2b72c085c3aa037")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
