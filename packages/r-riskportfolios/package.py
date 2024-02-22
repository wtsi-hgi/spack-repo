# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskportfolios(RPackage):
	"""Computation of Risk-Based Portfolios

	Collection of functions designed to compute risk-based portfolios as described 
    in Ardia et al. (2017) <doi:10.1007/s10479-017-2474-7> and Ardia et al. (2017) <doi:10.21105/joss.00171>.
	"""
	
	homepage = "https://github.com/ArdiaD/RiskPortfolios"
	cran = "RiskPortfolios" 

	version("2.1.7", md5="09ff7d78793aa3fd7c28b6bf2e799a73")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
