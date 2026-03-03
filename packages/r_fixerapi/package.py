# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFixerapi(RPackage):
	"""An R Client for the "Fixer.io" Currency API

	An R client for the "fixer.io" currency conversion and exchange 
  rate API. The API requires registration and some features are only available 
  on paid accounts. The full API documentation is available at 
  <https://fixer.io/documentation>.
	"""
	
	homepage = "https://docs.evanodell.com/fixerapi"
	cran = "fixerapi" 

	version("0.1.6", md5="e9e94fc4017d94c22e1d85db9eefd642")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
