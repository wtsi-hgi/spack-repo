# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSevenbridges2(RPackage):
	"""The 'Seven Bridges Platform' API Client

	R client and utilities for 'Seven Bridges Platform' API, from 'Cancer Genomics Cloud' 
    to other 'Seven Bridges' supported platforms. API documentation is hosted publicly 
    at <https://docs.sevenbridges.com/docs/the-api>.
	"""
	
	homepage = "https://www.sevenbridges.com"
	cran = "sevenbridges2" 

	version("0.1.0", md5="ead08436996d7d948c53ee44fe5cca7a", url="https://cran.r-project.org/src/contrib/sevenbridges2_0.1.0.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
