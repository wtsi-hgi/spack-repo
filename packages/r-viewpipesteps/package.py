# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViewpipesteps(RPackage):
	"""Create View Tabs of Pipe Chains

	Debugging pipe chains often consists of viewing the output after 
  each step. This package adds RStudio addins and two functions that allow 
  outputing each or select steps in a convenient way.
	"""
	
	cran = "ViewPipeSteps" 

	version("0.1.0", md5="6cdeaa4fd9d6bf3373f1c130937f3f71")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
