# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdjustedcranlogs(RPackage):
	"""Remove Automated and Repeated Downloads from 'RStudio' 'CRAN'
Download Logs

	Adjusts output of 'cranlogs' package to account for 'CRAN'-wide daily automated downloads and re-downloads caused by package updates.
	"""
	
	homepage = "https://github.com/tylermorganwall/adjustedcranlogs"
	cran = "adjustedcranlogs" 

	version("0.1.0", md5="58ba023ae6373cec4ec242c1f2b68bab")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cranlogs", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
