# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFredr(RPackage):
	"""An R Client for the 'FRED' API

	An R client for the 'Federal Reserve Economic Data'
    ('FRED') API <https://research.stlouisfed.org/docs/api/>.  Functions
    to retrieve economic time series and other data from 'FRED'.
	"""
	
	homepage = "https://github.com/sboysel/fredr"
	cran = "fredr" 

	version("2.1.0", md5="eae5d1d5d8f37deb81f030f36f411cd2")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
