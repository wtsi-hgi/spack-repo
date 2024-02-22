# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMort(RPackage):
	"""Identifying Potential Mortalities and Expelled Tags in Aquatic
Acoustic Telemetry Arrays

	A toolkit for identifying potential mortalities and expelled tags in aquatic acoustic telemetry arrays. 
    Designed for arrays with non-overlapping receivers. 
	"""
	
	homepage = "https://github.com/rosieluain/mort"
	cran = "mort" 

	version("0.0.1", md5="acaf40313bfc794aa2e8aba7b66c6e6a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
