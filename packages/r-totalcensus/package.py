# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTotalcensus(RPackage):
	"""Extract Decennial Census and American Community Survey Data

	Download summary files from Census Bureau <https://www2.census.gov/> 
    and extract data, in particular high resolution data at 
    block, block group, and tract level, from decennial census and 
    American Community Survey 1-year and 5-year estimates.
	"""
	
	homepage = "https://github.com/GL-Li/totalcensus"
	cran = "totalcensus" 

	version("0.6.6", md5="94df8969e98e2eaa0f1430e467b80a5c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-data-table@1.10.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
