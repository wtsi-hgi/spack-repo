# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgeeMixed(RPackage):
	"""Penalized Generalized Estimating Equations for Bivariate Mixed
Outcomes

	Perform simultaneous estimation and variable selection for correlated bivariate
    mixed outcomes (one continuous outcome and one binary outcome per cluster) using
    penalized generalized estimating equations. In addition, clustered Gaussian and binary
    outcomes can also be modeled. The SCAD, MCP, and LASSO penalties are supported.
    Cross-validation can be performed to find the optimal regularization parameter(s).
	"""
	
	homepage = "http://github.com/kaos42/pgee.mixed"
	cran = "pgee.mixed" 

	version("0.1.0", md5="452886f4ba45e74fc87cd7e8e1ab0088")

	depends_on("r-mvtnorm@1.0.5:", type=("build", "run"))
	depends_on("r-copula@0.999.15:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
