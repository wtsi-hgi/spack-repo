# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCols4all(RPackage):
	"""Colors for all

	Color palettes for all people, including those with color vision deficiency. Popular color palette series have been organized by type and have been scored on several properties such as color-blind-friendliness and fairness (i.e. do colors stand out equally?). Own palettes can also be loaded and analysed. Besides the common palette types (categorical, sequential, and diverging) it also includes bivariate color palettes. Furthermore, a color for missing values is assigned to each palette.
	"""
	
	homepage = "https://mtennekes.github.io/cols4all/"
	cran = "cols4all" 

	version("0.7-1", md5="50d97988ecc7a341adbba2c387220f3a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-colorspace@2.1:", type=("build", "run"))
	depends_on("r-spacesxyz", type=("build", "run"))
