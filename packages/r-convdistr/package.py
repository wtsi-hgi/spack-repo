# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvdistr(RPackage):
	"""Convolute Probabilistic Distributions

	Convolute probabilistic distributions using the random generator 
 function of each distribution. A new random number generator function is created that 
 perform the mathematical operation on the individual random samples from the 
 random generator function of each distribution. See the documentation for examples.
	"""
	
	homepage = "https://github.com/johnaponte/convdistr"
	cran = "convdistr" 

	version("1.6.1", md5="b66400efeda18b84bc749409105ac6fb")

	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shelf", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
