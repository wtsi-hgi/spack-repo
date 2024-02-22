# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeonos(RPackage):
	"""Basic Data Wrangling for NEON Observational Data

	NEON observational data are provided via the NEON Data Portal <https://www.neonscience.org> 
  and NEON API, and can be downloaded and reformatted by the 'neonUtilities' package. NEON observational data 
  (human-observed measurements, and analyses derived from human-collected samples, such as tree diameters and 
  algal chemistry) are published in a format consisting of one or more tabular data files. This package provides 
  tools for performing common operations on NEON observational data, including checking for duplicates and 
  joining tables.
	"""
	
	homepage = "https://github.com/NEONScience/NEON-OS-data-processing"
	cran = "neonOS" 

	version("1.0.0", md5="625bc7ff78f8fc550805038ddb7b6338")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
