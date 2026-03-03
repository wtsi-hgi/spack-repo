# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurrogateregression(RPackage):
	"""Surrogate Outcome Regression Analysis

	Performs estimation and inference on a partially missing target outcome (e.g. gene expression in an inaccessible tissue) while borrowing information from a correlated surrogate outcome (e.g. gene expression in an accessible tissue). Rather than regarding the surrogate outcome as a proxy for the target outcome, this package jointly models the target and surrogate outcomes within a bivariate regression framework. Unobserved values of either outcome are treated as missing data. In contrast to imputation-based inference, no assumptions are required regarding the relationship between the target and surrogate outcomes. Estimation in the presence of bilateral outcome missingness is performed via an expectation conditional maximization either algorithm. In the case of unilateral target missingness, estimation is performed using an accelerated least squares procedure. A flexible association test is provided for evaluating hypotheses about the target regression parameters. For additional details, see: McCaw ZR, Gaynor SM, Sun R, Lin X: "Leveraging a surrogate outcome to improve inference on a partially missing target outcome" <doi:10.1111/biom.13629>.
	"""
	
	cran = "SurrogateRegression" 

	version("0.6.0.1", md5="b218c9750c65f14c3923e3a5a255fb3b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
