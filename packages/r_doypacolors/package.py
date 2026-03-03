# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoypacolors(RPackage):
	"""Don't Overthink Your Palette of Colors

	Access diverse 'ggplot2'-compatible color palettes for simplified data visualization.
	"""
	
	homepage = "https://github.com/jmestret/DOYPAColors"
	cran = "DOYPAColors" 

	version("0.0.1", md5="3546e5fccc4d6b409032cdbee4b846a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
