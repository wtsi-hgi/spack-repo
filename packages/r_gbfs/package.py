# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbfs(RPackage):
	"""Interface with Live Bikeshare Data

	Supplies a set of functions to interface with bikeshare data
    following the General Bikeshare Feed Specification, allowing users to query
    and accumulate tidy datasets for specified cities/bikeshare programs.
	"""
	
	homepage = "https://github.com/simonpcouch/gbfs"
	cran = "gbfs" 

	version("1.3.9", md5="16acd2eeb23978e4787319b95d83605d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
