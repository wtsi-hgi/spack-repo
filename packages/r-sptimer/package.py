# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSptimer(RPackage):
	"""Spatio-Temporal Bayesian Modelling

	Fits, spatially predicts and temporally forecasts large amounts of space-time data using  [1] Bayesian Gaussian Process (GP) Models, [2] Bayesian Auto-Regressive (AR) Models, and [3] Bayesian Gaussian Predictive Processes (GPP) based AR Models for spatio-temporal big-n problems. Bakar and Sahu (2015) <doi:10.18637/jss.v063.i15>.
	"""
	
	cran = "spTimer" 

	version("3.3.2", md5="62ca8abd2ab899329f902abb67c32c0e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
