# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopdemo(RPackage):
	"""Demographic Modelling Using Projection Matrices

	Tools for modelling populations and demography using matrix projection models,
 with deterministic and stochastic model implementations. Includes population projection,
 indices of short- and long-term population size and growth, perturbation analysis,
 convergence to stability or stationarity, and diagnostic and manipulation tools.
	"""
	
	cran = "popdemo" 

	version("1.3-1", md5="c5503ccfe67124a3a4223da40a129828")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
