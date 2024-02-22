# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUncertainty(RPackage):
	"""Uncertainty Estimation and Contribution Analysis

	Implements the Gaussian method of first and second order, the Kragten numerical method and the Monte Carlo simulation method for uncertainty estimation and analysis.
	"""
	
	cran = "uncertainty" 

	version("0.2.0", md5="267bfda809cb5f908f8cba1b13dceba9")

	depends_on("r-mvtnorm@0.9:", type=("build", "run"))
	depends_on("r-triangle@0.7:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
