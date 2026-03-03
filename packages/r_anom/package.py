# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnom(RPackage):
	"""Analysis of Means

	Analysis of means (ANOM) as used in technometrical computing. The package takes results from multiple comparisons with the grand mean (obtained with 'multcomp', 'SimComp', 'nparcomp', or 'MCPAN') or corresponding simultaneous confidence intervals as input and produces ANOM decision charts that illustrate which group means deviate significantly from the grand mean.
	"""
	
	homepage = "https://github.com/PhilipPallmann/ANOM"
	cran = "ANOM" 

	version("0.5", md5="3f3963281454dc550afb9739193f1f61")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mcpan", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-nparcomp", type=("build", "run"))
	depends_on("r-simcomp", type=("build", "run"))
