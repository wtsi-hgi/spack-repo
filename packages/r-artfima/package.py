# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArtfima(RPackage):
	"""ARTFIMA Model Estimation

	Fit and simulate ARTFIMA. Theoretical autocovariance function and spectral density function for stationary ARTFIMA.
	"""
	
	homepage = "http://www.stats.uwo.ca/faculty/aim"
	cran = "artfima" 

	version("1.5", md5="8b29c5ba127c5d22c5933fbf9749a2d9")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-ltsa", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
