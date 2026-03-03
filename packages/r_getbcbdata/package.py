# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetbcbdata(RPackage):
	"""Imports Datasets from BCB (Central Bank of Brazil) using Its
Official API

	Downloads and organizes datasets using BCB's API <https://www.bcb.gov.br/>. Offers options for caching with the 'memoise' package and
    , multicore/multisession with 'furrr' and format of output data (long/wide). 
	"""
	
	homepage = "https://github.com/msperlin/GetBCBData/"
	cran = "GetBCBData" 

	version("0.7.0", md5="b4d0ac2b405f1e94794a5979daa67ebe")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
