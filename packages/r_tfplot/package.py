# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfplot(RPackage):
	"""Time Frame User Utilities

	Utilities for simple manipulation and quick  	
	plotting of time series data. These utilities use the 'tframe' package
	which provides a programming kernel for time series. Extensions to
	'tframe' provided in 'tframePlus' can also be used. See the Guide
	vignette for examples.
	"""
	
	homepage = "http://tsanalysis.r-forge.r-project.org/"
	cran = "tfplot" 

	version("2021.6-1", md5="b7b842a5f7ac77956d2bf560a7ab05fa")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-tframe", type=("build", "run"))
