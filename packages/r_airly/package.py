# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirly(RPackage):
	"""R Wrapper for 'Airly' API

	Get information about air quality using 'Airly' <https://airly.eu/> API through R.
	"""
	
	homepage = "https://github.com/piotrekjanus/aiRly"
	cran = "aiRly" 

	version("0.1.0", md5="1b7f4f79ac1b88774e646c777b800365")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
