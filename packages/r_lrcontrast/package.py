# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrcontrast(RPackage):
	"""Dose Response Signal Detection under Model Uncertainty

	Provides functions for calculating test statistics, simulating quantiles 
	and simulating p-values of likelihood ratio contrast tests in regression models 
	with a lack of identifiability.
	"""
	
	cran = "LRcontrast" 

	version("1.0", md5="a5f450d84aee07e211e4c110838fdc85")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dosefinding", type=("build", "run"))
