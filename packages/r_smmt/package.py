# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmmt(RPackage):
	"""The Swiss Municipal Data Merger Tool Maps Municipalities Over
Time

	In Switzerland, the landscape of municipalities is changing rapidly
  mainly due to mergers. The Swiss Municipal Data Merger Tool 
  automatically detects these mutations and maps municipalities over time, i.e. municipalities of an old state
  to municipalities of a new state. This functionality is helpful when working 
  with datasets that are based on different spatial references. The package's idea and use 
  case is discussed in the following article: <https://onlinelibrary.wiley.com/doi/full/10.1111/spsr.12487>.
	"""
	
	homepage = "https://github.com/ValValetl/SMMT"
	cran = "SMMT" 

	version("1.1.0", md5="e44c8fe2f4ed2704a0a010d3f9247f1d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
