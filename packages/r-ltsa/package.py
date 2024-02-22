# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtsa(RPackage):
	"""Linear Time Series Analysis

	Methods of developing linear time series modelling.
 Methods are given for loglikelihood computation, forecasting
  and simulation.
	"""
	
	homepage = "http://www.stats.uwo.ca/faculty/aim"
	cran = "ltsa" 

	version("1.4.6", md5="7744dde6afc5ea6a370dde3a01d4b0fe")

	depends_on("r@2.1:", type=("build", "run"))
