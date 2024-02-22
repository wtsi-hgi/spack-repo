# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRingostat(RPackage):
	"""Load Data from 'Ringostat API'

	Loading calls data from 'Ringostat API'. 
    See <https://help.ringostat.com/knowledge-base/article/integration-with-ringostat-via-api>.
	"""
	
	cran = "ringostat" 

	version("0.1.5", md5="fa1bc4deda401b3e25be3c20fe7e04b9")

	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
