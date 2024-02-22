# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWildcard(RPackage):
	"""Templates for Data Frames

	Generate data frames from templates.
	"""
	
	homepage = "https://github.com/wlandau/wildcard"
	cran = "wildcard" 

	version("1.1.0", md5="f73488ffc91988ba80956a2492e90950")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
