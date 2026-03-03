# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcdr(RPackage):
	"""Utilities for Interacting with the 'CCTE' APIs

	Access chemical, hazard, and bioactivity data from the Center for
   Computational Toxicology and Exposure ('CCTE') APIs 
   <https://api-ccte.epa.gov/docs/>. 'ccdR' was developed to streamline the 
   process of accessing the information available through the 'CCTE' APIs 
   without requiring prior knowledge of how to use APIs. All data is also 
   available on the CompTox Chemical Dashboard ('CCD')
   <https://comptox.epa.gov/dashboard/>. 
	"""
	
	homepage = "https://github.com/USEPA/ccdR"
	cran = "ccdR" 

	version("1.0.0", md5="edfc6ad3e48962369edae92170a37c72")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
