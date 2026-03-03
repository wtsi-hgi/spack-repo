# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissdiag(RPackage):
	"""Comparing Observed and Imputed Values under MAR and MCAR

	Implements the computation of discrepancy statistics summarizing differences between the density of imputed and observed values and the construction of weights to balance covariates that are part of the missing data mechanism as described in Marbach (2021) <arXiv:2107.05427>. 
	"""
	
	homepage = "https://github.com/sumtxt/missDiag/"
	cran = "missDiag" 

	version("1.0.1", md5="dabf3811de3d69055cf454aaad70b479")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-formula@1.2.3:", type=("build", "run"))
	depends_on("r-cobalt@4.1:", type=("build", "run"))
