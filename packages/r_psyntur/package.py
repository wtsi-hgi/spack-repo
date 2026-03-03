# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsyntur(RPackage):
	"""Helper Tools for Teaching Statistical Data Analysis

	Provides functions and data-sets that are helpful 
  for teaching statistics and data analysis. It was originally designed for use
  when teaching students in the Psychology Department at Nottingham Trent University.
	"""
	
	cran = "psyntur" 

	version("0.1.0", md5="a30b5e02888458496b299dd20f41a5b5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-formula-tools@1.7.1:", type=("build", "run"))
	depends_on("r-ggally@2.1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-ggthemes@4.2.4:", type=("build", "run"))
	depends_on("r-psych@2.1.6:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-effsize@0.8.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
	depends_on("r-ez@4.4:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.1:", type=("build", "run"))
