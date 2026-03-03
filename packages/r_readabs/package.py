# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadabs(RPackage):
	"""Download and Tidy Time Series Data from the Australian Bureau of
Statistics

	Downloads, imports, and tidies time series data from the 
    Australian Bureau of Statistics <https://www.abs.gov.au/>.
	"""
	
	homepage = "https://github.com/mattcowgill/readabs"
	cran = "readabs" 

	version("0.4.14", md5="be85b5f9d68081c15aa24301c9316923")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readxl@1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-hutils@1.5:", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
