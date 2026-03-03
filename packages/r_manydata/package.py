# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManydata(RPackage):
	"""A Portal for Global Governance Data

	This is the core package for the many packages universe.
    It includes functions to help researchers work with and contribute to 
    event datasets on global governance.
	"""
	
	homepage = "https://github.com/globalgov/manydata"
	cran = "manydata" 

	version("0.9.2", md5="39f65303574b9d69a0b4386acfc0affa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-messydates", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
