# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCprobit(RPackage):
	"""Conditional Probit Model for Analysing Continuous Outcomes

	Implements the three-step workflow for robust analysis of change in 
    two repeated measurements of continuous outcomes, described in Ning et al.
    (in press), "Robust estimation of the effect of an exposure on the change in
    a continuous outcome", BMC Medical Research Methodology.
	"""
	
	cran = "cprobit" 

	version("1.0.2", md5="dec0ffdc3260d792a249dd8f6e66a7f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
