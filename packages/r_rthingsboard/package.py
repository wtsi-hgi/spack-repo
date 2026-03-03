# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRthingsboard(RPackage):
	"""'ThingsBoard' API

	The goal of 'Rthingsboard' is to provide interaction with the API of 'ThingsBoard' (<https://thingsboard.io/>), an open-source IoT platform for device management, data collection, processing and visualization.
	"""
	
	homepage = "https://ddorch.github.io/Rthingsboard/"
	cran = "Rthingsboard" 

	version("0.2.7", md5="725a2c6ff623a3e439e0f5b624fd5be4")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
