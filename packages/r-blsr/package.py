# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlsr(RPackage):
	"""Make Requests from the Bureau of Labor Statistics API

	Implements v2 of the B.L.S. API for requests of survey information
  and time series data through 3-tiered API that allows users to interact with
  the raw API directly, create queries through a functional interface, and
  re-shape the data structures returned to fit common uses. The API definition 
  is located at: <https://www.bls.gov/developers/api_signature_v2.htm>.
	"""
	
	homepage = "https://github.com/groditi/blsR"
	cran = "blsR" 

	version("0.5.0", md5="4a21847cbdd6991aba2d8db060e6dcdd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
