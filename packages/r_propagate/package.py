# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPropagate(RPackage):
	"""Propagation of Uncertainty

	Propagation of uncertainty using higher-order Taylor expansion and Monte Carlo simulation.
	"""
	
	cran = "propagate" 

	version("1.0-6", md5="3531faaf8babd4b7f7e2c52ffb77f96c")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
