# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmhc(RPackage):
	"""Access, Retrieve, and Work with CMHC Data

	Wrapper around the Canadian Mortgage and Housing Corporation (CMHC) web interface. It enables programmatic and reproducible access to a wide variety of housing data from CMHC.
	"""
	
	homepage = "https://github.com/mountainMath/cmhc"
	cran = "cmhc" 

	version("0.2.7", md5="17d3187decbfec24655fcff386551562")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-digest@0.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-aws-s3", type=("build", "run"))
