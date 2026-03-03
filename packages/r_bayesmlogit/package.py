# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmlogit(RPackage):
	"""A Multistate Life Table (MSLT) Methodology Based on Bayesian
Approach

	Create life tables with a Bayesian approach, which can be very useful for modelling a complex health process when considering multiple predisposing factors and multiple coexisting health conditions. Details for this method can be found in: Lynch, Scott, et al., (2022) <doi:10.1177/00811750221112398>; Zang, Emma, et al., (2022) <doi:10.1093/geronb/gbab149>.
	"""
	
	cran = "bayesmlogit" 

	version("1.0.1", md5="f98f85079d1dcf14968a938e43eb5c3f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
