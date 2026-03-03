# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNts(RPackage):
	"""Nonlinear Time Series Analysis

	Simulation, estimation, prediction procedure, and model identification methods for nonlinear time series analysis, including threshold autoregressive models, Markov-switching models, convolutional functional autoregressive models, nonlinearity tests, Kalman filters and various sequential Monte Carlo methods. More examples and details about this package can be found in the book "Nonlinear Time Series Analysis" by Ruey S. Tsay and Rong Chen, John Wiley & Sons, 2018 (ISBN: 978-1-119-26407-1).
	"""
	
	cran = "NTS" 

	version("1.1.3", md5="44c7a723d736b1fc4c2e1cb10dd3a5d1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dlm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mswm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
