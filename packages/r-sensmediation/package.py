# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensmediation(RPackage):
	"""Parametric Estimation and Sensitivity Analysis of Direct and
Indirect Effects

	We implement functions to estimate and perform sensitivity analysis to unobserved confounding of direct and indirect effects introduced in Lindmark, de Luna and Eriksson (2018) <doi:10.1002/sim.7620>. The estimation and sensitivity analysis are parametric, based on probit and/or linear regression models. Sensitivity analysis is implemented for unobserved confounding of the exposure-mediator, mediator-outcome and exposure-outcome relationships. 
	"""
	
	cran = "sensmediation" 

	version("0.3.0", md5="f21ca218931df2a654882309a4ab4b44")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-maxlik@1.3.4:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.8:", type=("build", "run"))
