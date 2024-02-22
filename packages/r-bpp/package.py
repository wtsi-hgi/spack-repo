# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpp(RPackage):
	"""Computations Around Bayesian Predictive Power

	Implements functions to update Bayesian Predictive Power Computations after not stopping a clinical trial at an interim analysis. Such an interim analysis can either be blinded or unblinded. Code is provided for Normally distributed endpoints with known variance, with a prominent example being the hazard ratio.
	"""
	
	cran = "bpp" 

	version("1.0.4", md5="375aed2cd46ed7e4cfaa5f64500182d2")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
