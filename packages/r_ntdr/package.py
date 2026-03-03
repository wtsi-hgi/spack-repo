# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNtdr(RPackage):
	"""Retrieve Data from the National Transit Database

	Downloads the latest 'National Transit Database' 
    data, processes it, and returns in a tidy data format.
	"""
	
	homepage = "https://vgxhc.github.io/ntdr/"
	cran = "ntdr" 

	version("0.3.3", md5="0a9839a615cb912a6657f2d02c3d55db")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
