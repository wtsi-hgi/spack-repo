# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLink2gi(RPackage):
	"""Linking Geographic Information Systems, Remote Sensing and Other
Command Line Tools

	Functions to simplify the linking of open source GIS and remote sensing related command line interfaces.
	"""
	
	homepage = "https://github.com/r-spatial/link2GI/"
	cran = "link2GI" 

	version("0.5-3", md5="211dc9c5962888bf442b2428941b99a5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-sf@0.9:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
