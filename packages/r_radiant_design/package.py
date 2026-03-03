# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadiantDesign(RPackage):
	"""Design Menu for Radiant: Business Analytics using R and Shiny

	The Radiant Design menu includes interfaces for design of
    experiments, sampling, and sample size calculation. The application extends
    the functionality in 'radiant.data'.
	"""
	
	homepage = "https://github.com/radiant-rstats/radiant.design/"
	cran = "radiant.design" 

	version("1.6.1", md5="e5c4e3be4d6b9b73b7a864c4dbd932e0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-radiant-data@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-algdesign@1.1.7.3:", type=("build", "run"))
	depends_on("r-import@1.1:", type=("build", "run"))
	depends_on("r-pwr@1.1.2:", type=("build", "run"))
	depends_on("r-randomizr@0.20:", type=("build", "run"))
	depends_on("r-mvtnorm@1.2:", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
