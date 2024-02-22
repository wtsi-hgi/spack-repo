# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDse(RPackage):
	"""Dynamic Systems Estimation (Time Series Package)

	Tools for multivariate, linear, time-invariant,
	time series models. This includes ARMA and state-space representations,
	and methods for converting between them. It also includes simulation
	methods and several estimation functions. The package has functions 
	for looking at model roots, stability, and forecasts at different 
	horizons. The ARMA model representation is general, so that VAR, VARX, 
	ARIMA, ARMAX, ARIMAX can all be considered to be special cases. Kalman
	filter and smoother estimates can be obtained from the state space
	model, and state-space model reduction techniques are implemented. 
	An introduction and User's Guide is available in a vignette.
	"""
	
	homepage = "http://tsanalysis.r-forge.r-project.org/"
	cran = "dse" 

	version("2020.2-1", md5="e74dac047ec2346c3b66d6958cdaf4bc")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-tfplot", type=("build", "run"))
	depends_on("r-tframe@2007.5.3:", type=("build", "run"))
	depends_on("r-setrng@2004.4.1:", type=("build", "run"))
