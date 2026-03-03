# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSc2api(RPackage):
	"""Blizzard SC2 API Wrapper

	A wrapper for Blizzard's Starcraft II (a 2010 real-time strategy game) Application Programming Interface (API). All documented API calls are implemented in an easy-to-use and consistent manner.
	"""
	
	cran = "SC2API" 

	version("1.0.0", md5="38b5bdd2f0c95c8c3a1f48aace1705d7")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
