# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REyetrackingr(RPackage):
	"""Eye-Tracking Data Analysis

	Addresses tasks along the pipeline from raw
    data to analysis and visualization for eye-tracking data. Offers several
    popular types of analyses, including linear and growth curve time analyses,
    onset-contingent reaction time analyses, as well as several non-parametric
    bootstrapping approaches. For references to the approach see Mirman, 
    Dixon & Magnuson (2008) <doi:10.1016/j.jml.2007.11.006>, and
    Barr (2008) <doi:10.1016/j.jml.2007.09.002>.
	"""
	
	homepage = "http://samforbes.me/eyetrackingR/"
	cran = "eyetrackingR" 

	version("0.2.1", md5="8fd93c9da121765e50db918a3f3d3b2c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-broom@0.3.7:", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-lazyeval@0.1.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-zoo@1.7.12:", type=("build", "run"))
	depends_on("r-tidyr@0.3.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
