# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgrain(RPackage):
	"""A Rainclouds Geom for 'ggplot2'

	The 'geom_rain()' function adds different geoms together using 'ggplot2' to create raincloud plots. 
	"""
	
	homepage = "https://github.com/njudd/ggrain"
	cran = "ggrain" 

	version("0.0.4", md5="8e24f1f21eac678fe6b1951e61022701")

	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gghalves", type=("build", "run"))
	depends_on("r-ggpp@0.5.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
