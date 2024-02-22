# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTqk(RPackage):
	"""Get Financial Data in Korea

	Enables the acquisition of Korean financial market data, 
            designed to integrate seamlessly with the 'tidyquant' package.
	"""
	
	homepage = "https://github.com/mrchypark/tqk"
	cran = "tqk" 

	version("0.1.8", md5="be42c0ea902f40e55f7bd935426e0bca")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
