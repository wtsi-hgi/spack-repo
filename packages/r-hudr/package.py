# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHudr(RPackage):
	"""Providing Data from the US Department of Housing and Urban
Development

	Provides functions to access data from the US Department of Housing and Urban Development <https://www.huduser.gov/portal/dataset/fmr-api.html>.
	"""
	
	cran = "hudr" 

	version("1.2.0", md5="127660249e62a9949e7af3c6d9f72f30")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
