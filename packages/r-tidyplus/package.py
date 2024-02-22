# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyplus(RPackage):
	"""Additional 'tidyverse' Functions

	Provides functions such as str_crush(), add_missing_column(), 
  coalesce_data() and drop_na_all() that complement 'tidyverse' functionality
  or functions that provide alternative behaviors such as if_else2()
  and str_detect2().
	"""
	
	homepage = "https://github.com/poissonconsulting/tidyplus"
	cran = "tidyplus" 

	version("0.0.2", md5="0985ff17c401c5692abb2bbe6dc9f9bf")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
