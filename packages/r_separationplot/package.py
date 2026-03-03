# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeparationplot(RPackage):
	"""Separation Plots

	Visual representations of model fit or predictive success in the form of "separation plots."  See Greenhill, Brian, Michael D. Ward, and Audrey Sacks. "The separation plot: A new visual method for evaluating the fit of binary models." American Journal of Political Science 55.4 (2011): 991-1002.
	"""
	
	cran = "separationplot" 

	version("1.4", md5="4485e15bd560d1b981ec28077ffd28fa")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
