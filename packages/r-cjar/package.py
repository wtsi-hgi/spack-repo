# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCjar(RPackage):
	"""R Client for 'Customer Journey Analytics' ('CJA') API

	Connect to the 'CJA' API, which powers 'CJA Workspace' <https://github.com/AdobeDocs/cja-apis>. The package 
             was developed with the analyst in mind and will continue to be 
             developed with the guiding principles of iterative, repeatable, 
             timely analysis. New features are actively being developed and we 
             value your feedback and contribution to the process. 
	"""
	
	cran = "cjar" 

	version("0.1.2", md5="abe1de48aa3fe91ef8497ee5b344e832")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jose", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
