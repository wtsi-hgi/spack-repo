# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDivseg(RPackage):
	"""Calculate Diversity and Segregation Indices

	Implements common measures of diversity and spatial segregation. This package has tools to compute the majority of measures are reviewed in Massey and Denton (1988) <doi:10.2307/2579183>. Multiple common measures of within-geography diversity are implemented as well. All functions operate on data frames with a 'tidyselect' based workflow.
	"""
	
	homepage = "https://github.com/christopherkenny/divseg/"
	cran = "divseg" 

	version("0.0.5", md5="30ee40fefcc3cfb96a6fed02d3fffb70")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
