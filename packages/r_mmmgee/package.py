# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmmgee(RPackage):
	"""Simultaneous Inference for Multiple Linear Contrasts in GEE
Models

	Provides global hypothesis tests, multiple testing procedures and simultaneous confidence intervals for multiple linear contrasts of regression
	coefficients in a single generalized estimating equation (GEE) model or across multiple GEE models. GEE models are fit by a modified version of the 'geeM' package.
	"""
	
	cran = "mmmgee" 

	version("1.20", md5="e0b4b12451f38328f33d6727a9ce2362")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
