# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestdimorph(RPackage):
	"""Analysis of the Interpopulation Difference in Degree of Sexual
Dimorphism Using Summary Statistics

	Offers a solution for the unavailability of raw data in most anthropological studies by facilitating the calculations of several sexual dimorphism related analyses using the published summary statistics of metric data (mean, standard deviation and sex specific sample size) as illustrated by the works of Relethford, J. H., & Hodges, D. C. (1985) <doi:10.1002/ajpa.1330660105>, Greene, D. L. (1989) <doi:10.1002/ajpa.1330790113> and Konigsberg, L. W. (1991) <doi:10.1002/ajpa.1330840110>.
	"""
	
	cran = "TestDimorph" 

	version("0.5.8", md5="fbecad1166ddcaf475461a98c683b22d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-morpho", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
