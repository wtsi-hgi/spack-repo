# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbdecomp(RPackage):
	"""Estimation of the Proportion of SB Explained by Confounders

	Uses parametric and nonparametric methods to quantify the proportion of the estimated selection bias (SB) explained by each observed confounder when estimating propensity score weighted treatment effects. Parast, L and Griffin, BA (2020). "Quantifying the Bias due to Observed Individual Confounders in Causal Treatment Effect Estimates". Statistics in Medicine, 39(18): 2447- 2476 <doi: 10.1002/sim.8549>.
	"""
	
	cran = "SBdecomp" 

	version("1.2", md5="877b6e8b489810d912c33b9451a2be8e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-twang", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
