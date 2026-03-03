# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGesttools(RPackage):
	"""General Purpose G-Estimation for End of Study or Time-Varying
Outcomes

	Provides a series of general purpose tools to perform g-estimation using the methods described in Sjolander and Vansteelandt (2016) <doi:10.1515/em-2015-0005> and Dukes and Vansteelandt <doi:10.1093/aje/kwx347>. The package allows for g-estimation in a wide variety of circumstances, including an end of study or time-varying outcome, and an exposure that is a binary, continuous, or a categorical variable with three or more categories. The package also supports g-estimation with time-varying causal effects and effect modification by a confounding variable.
	"""
	
	homepage = "https://github.com/danieltompsett/gesttools"
	cran = "gesttools" 

	version("1.3.0", md5="bd3220fd3440e5268e6b37e4fc020567")

	depends_on("r-datacombine", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-geem", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
