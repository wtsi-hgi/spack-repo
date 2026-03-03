# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSteps(RPackage):
	"""Spatially- and Temporally-Explicit Population Simulator

	Software to simulate population change across space and time. Visintin et al. (2020) <doi:10.1111/2041-210X.13354>.
	"""
	
	homepage = "https://github.com/steps-dev/steps"
	cran = "steps" 

	version("1.3.0", md5="be370b92345a68a6247e6478f138fcd0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-rastervis", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-memuse", type=("build", "run"))
