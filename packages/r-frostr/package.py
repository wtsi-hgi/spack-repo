# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrostr(RPackage):
	"""R API to MET Norway's 'Frost' API

	An R API to MET Norway's 'Frost' API <https://frost.met.no/index.html> 
    to retrieve data as data frames. The 'Frost' API, and the underlying data, is 
    made available by the Norwegian Meteorological Institute (MET Norway). The data
    and products are distributed under the 
    Norwegian License for Open Data 2.0 (NLOD) <https://data.norge.no/nlod/en/2.0>
    and Creative Commons 4.0 <https://creativecommons.org/licenses/by/4.0/>.
	"""
	
	cran = "frostr" 

	version("0.2.0", md5="860eb53af29dcf0cf731601ed43b8eb0")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
