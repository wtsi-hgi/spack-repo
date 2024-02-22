# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilebin(RPackage):
	"""Wrapper for the Filebin File Sharing API

	A wrapper for the Filebin API. Filebin implements convenient file
    sharing on the web.
	"""
	
	cran = "filebin" 

	version("0.0.6", md5="e64f3c84bc0197aa3c41f68d809f77b8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
