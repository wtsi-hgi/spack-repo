# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaturalearth(RPackage):
	"""World Map Data from Natural Earth

	Facilitates mapping by making natural earth map data from <https://www.naturalearthdata.com/> more easily available to R users.
	"""
	
	homepage = "https://docs.ropensci.org/rnaturalearth/"
	cran = "rnaturalearth" 

	version("1.0.1", md5="3b8789b1603823e57c8b8237cf1317f9")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sf@0.3.4:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
