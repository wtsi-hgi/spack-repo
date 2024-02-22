# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrettymapr(RPackage):
	"""Scale Bar, North Arrow, and Pretty Margins in R

	Automates the process of creating a scale bar and north arrow in
    any package that uses base graphics to plot in R. Bounding box tools help find
    and manipulate extents. Finally, there is a function to automate the process
    of setting margins, plotting the map, scale bar, and north arrow, and resetting
    graphic parameters upon completion.
	"""
	
	homepage = "https://github.com/paleolimbot/prettymapr"
	cran = "prettymapr" 

	version("0.2.4", md5="51852996fccfc384e6ee2866deb75890")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
