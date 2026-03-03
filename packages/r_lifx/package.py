# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifx(RPackage):
	"""Control 'LIFX' Smart Light Bulbs

	Allows you to read and change the state of 'LIFX' smart light bulbs via the 'LIFX' developer api <https://api.developer.lifx.com/>.
    Covers most 'LIFX' api endpoints, including changing light color and brightness, selecting lights by id, group or location as well as activating effects.
	"""
	
	cran = "lifx" 

	version("0.2.0", md5="10df3854822cba57832a9a3ea824ea80")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
