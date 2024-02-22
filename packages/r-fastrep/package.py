# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastrep(RPackage):
	"""Time-Saving Package for Creating Reports

	Provides  templates for reports in 'rmarkdown' and 
     functions to create tables and summaries of data.
	"""
	
	cran = "fastrep" 

	version("0.7", md5="b86f5c772b98c6519f69a126c762d7d5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
