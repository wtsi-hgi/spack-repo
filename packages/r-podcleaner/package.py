# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPodcleaner(RPackage):
	"""Legacy Scottish Post Office Directories Cleaner

	Attempts to clean optical character recognition (OCR) errors in 
  legacy Scottish Post Office Directories. Further attempts to match records from 
  trades and general directories.  
	"""
	
	cran = "podcleaner" 

	version("0.1.2", md5="e0f257a349bd4e222a025e84ccb9ba0f")

	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-fuzzyjoin@0.1.6:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-readr@2.0.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.12:", type=("build", "run"))
	depends_on("r-stringi@1.7.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.5:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
