# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunctiondepends(RPackage):
	"""Find Functions and their Dependencies

	Find functions in an unstructured directory and explore their dependencies. 
    Sourcing of R source files is performed without side-effects: from R scripts that have 
    executable code and function definitions only functions are sourced. 
	"""
	
	cran = "functiondepends" 

	version("0.2.3", md5="cd9a669c735eaaad93e65e961b1d2eb9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
