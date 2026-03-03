# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlipbookr(RPackage):
	"""Parses Code, Creates Partial Code Builds, Delivers Code Movie

	Flipbooks present code step-by-step and side-by-side with its output.  'flipbookr' helps creators build flipbooks efficiently because code pipelines are automatically parsed and prepped for presentation as flipbooks. 
	"""
	
	cran = "flipbookr" 

	version("0.1.0", md5="e3f1e15bb057a916fc21856486868088")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
