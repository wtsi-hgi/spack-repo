# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConnectapi(RPackage):
	"""Utilities for Interacting with the 'Posit Connect' Server API

	Provides a helpful 'R6' class and methods for interacting with 
    the 'Posit Connect' Server API along with some meaningful utility functions
    for regular tasks. API documentation varies by 'Posit Connect' installation
    and version, but the latest documentation is also hosted publicly at 
    <https://docs.posit.co/connect/api/>.
	"""
	
	homepage = "https://github.com/rstudio/connectapi"
	cran = "connectapi" 

	version("0.1.3.1", md5="8058d89bd38484fab08c5bc52d155aff")

	depends_on("r-config", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang@0.4.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
