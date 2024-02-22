# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHexfinder(RPackage):
	"""Find Hex Logos for CRAN Packages

	Scavenge the web for possible hex logos for CRAN packages.
	"""
	
	homepage = "https://pedrocsilva.com"
	cran = "hexFinder" 

	version("0.8.2", md5="c456c384d5d822cb24ce0831e1889f21")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hexsticker", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pkgsearch", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
