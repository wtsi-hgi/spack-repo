# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGovinfor(RPackage):
	"""A 'GovInfo' API Wrapper

	Access data provided by the United States Government Publishing Office (GPO) 'GovInfo' API (<https://github.com/usgpo/api>).
	"""
	
	homepage = "https://github.com/blackerby/govinfoR"
	cran = "govinfoR" 

	version("0.0.3", md5="b30da80137ae818d89a80394c650f2de")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
