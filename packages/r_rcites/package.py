# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcites(RPackage):
	"""R Interface to the Species+ Database

	A programmatic interface to the Species+ <https://speciesplus.net/> database via the Species+/CITES Checklist API <https://api.speciesplus.net/>.
	"""
	
	homepage = "https://docs.ropensci.org/rcites/"
	cran = "rcites" 

	version("1.3.0", md5="33e2cb0f281ea313e1407963219ce884")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
