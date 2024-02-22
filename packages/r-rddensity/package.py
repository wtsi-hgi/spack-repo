# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRddensity(RPackage):
	"""Manipulation Testing Based on Density Discontinuity

	Density discontinuity testing (a.k.a. manipulation testing) is commonly employed in regression discontinuity designs and other program evaluation settings to detect perfect self-selection (manipulation) around a cutoff where treatment/policy assignment changes. This package implements manipulation testing procedures using the local polynomial density estimators: rddensity() to construct test statistics and p-values given a prespecified cutoff, rdbwdensity() to perform data-driven bandwidth selection, and rdplotdensity() to construct density plots.
	"""
	
	cran = "rddensity" 

	version("2.5", md5="2da32ef70b0362d02e06a3845881527f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lpdensity@2.2:", type=("build", "run"))
