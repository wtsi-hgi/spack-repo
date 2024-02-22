# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIadf(RPackage):
	"""Analysis of Intra Annual Density Fluctuations

	Calculate false ring proportions from data frames of intra annual 
  density fluctuations.
	"""
	
	homepage = "https://github.com/konradmayer/iadf"
	cran = "iadf" 

	version("0.1.2", md5="75ec0f8a63755f83d046c02b3a35e547")

	depends_on("r-manipulate", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
