# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpticut(RPackage):
	"""Likelihood Based Optimal Partitioning and Indicator Species
Analysis

	Likelihood based optimal partitioning and indicator
  species analysis. Finding the best binary partition for each species
  based on model selection, with the possibility to take into account
  modifying/confounding variables as described
  in Kemencei et al. (2014) <doi:10.1556/ComEc.15.2014.2.6>.
  The package implements binary and multi-level response models,
  various measures of uncertainty, Lorenz-curve based thresholding,
  with native support for parallel computations.
	"""
	
	homepage = "https://github.com/psolymos/opticut"
	cran = "opticut" 

	version("0.1-2", md5="d2c957c08d4b9a264cfd82780ee64dc4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-pbapply@1.3.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-resourceselection@0.3.2:", type=("build", "run"))
	depends_on("r-mefa4", type=("build", "run"))
