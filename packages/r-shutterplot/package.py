# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShutterplot(RPackage):
	"""The R Shutter Plot Package

	Shows the scatter plot along with the fitted regression lines. It 
  depicts min, max, the three quartiles, mean, and sd for each variable.
  It also depicts sd-line, sd-box, r, r-square, prediction boundaries, and regression outliers.  
	"""
	
	cran = "shutterplot" 

	version("0.1.0", md5="2f99e76c8e376325bb15ed9f37cc07dd")

	depends_on("r@3.1:", type=("build", "run"))
