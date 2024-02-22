# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatarobot(RPackage):
	"""'DataRobot' Predictive Modeling API

	For working with the 'DataRobot' predictive modeling platform's API <https://www.datarobot.com/>.
	"""
	
	cran = "datarobot" 

	version("2.18.5", md5="da1b9fc711598bdbe5e4d7e0a86a0d5d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr@1.2:", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
	depends_on("r-yaml@2.1.19:", type=("build", "run"))
