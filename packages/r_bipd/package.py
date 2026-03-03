# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBipd(RPackage):
	"""Bayesian Individual Patient Data Meta-Analysis using 'JAGS'

	We use a Bayesian approach to run individual patient data meta-analysis and network meta-analysis using 'JAGS'. The methods incorporate shrinkage methods and calculate patient-specific treatment effects as described in Seo et al. (2021) <DOI:10.1002/sim.8859>. This package also includes user-friendly functions that impute missing data in an individual patient data using mice-related packages.
	"""
	
	cran = "bipd" 

	version("0.3", md5="aae03d9b65cf8a0b24353aefea8b0985")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rjags@4.6:", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
