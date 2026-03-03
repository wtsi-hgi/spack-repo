# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeocacher(RPackage):
	"""Tools for Geocaching

	Tools for solving common geocaching puzzle types, and other
    Geocaching-related tasks.
	"""
	
	cran = "geocacheR" 

	version("0.1.0", md5="449091de83e548436a7f46eb38c4d6c4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-threewords", type=("build", "run"))
