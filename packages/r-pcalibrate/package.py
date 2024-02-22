# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcalibrate(RPackage):
	"""Bayesian Calibrations of p-Values

	Implements transformations of p-values to the smallest possible Bayes factor within the specified class of alternative hypotheses, as described in Held & Ott (2018, <doi:10.1146/annurev-statistics-031017-100307>). Covers several common testing scenarios such as z-tests, t-tests, likelihood ratio tests and the F-test. 
	"""
	
	cran = "pCalibrate" 

	version("0.2-1", md5="e5f640c333816506e9c0cee653ddae54")

	depends_on("r-exact2x2", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
