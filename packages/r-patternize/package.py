# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatternize(RPackage):
	"""Quantification of Color Pattern Variation

	Quantification of variation in organismal color patterns as
    obtained from image data. Patternize defines homology between pattern positions
    across images either through fixed landmarks or image registration. Pattern
    identification is performed by categorizing the distribution of colors using RGB
    thresholds or image segmentation.
	"""
	
	homepage = "https://github.com/StevenVB12/patternize"
	cran = "patternize" 

	version("0.0.5", md5="85c1a072f4bffb0cf7ca23e03024cb84")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-morpho", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-rniftyreg", type=("build", "run"))
	depends_on("r-geomorph", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
