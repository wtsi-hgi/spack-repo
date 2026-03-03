# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPieceexpintensity(RPackage):
	"""Bayesian Model to Find Changepoints Based on Rates and Count
Data

	This function fits a reversible jump Bayesian piecewise exponential model that also includes the intensity of each event considered along with the rate of events.
	"""
	
	cran = "PieceExpIntensity" 

	version("1.0.4", md5="d791f3b0ab0eeafc90c19b7c2e9f3d7d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
