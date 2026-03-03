# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisprity(RPackage):
	"""Measuring Disparity

	A modular package for measuring disparity (multidimensional space occupancy). Disparity can be calculated from any matrix defining a multidimensional space. The package provides a set of implemented metrics to measure properties of the space and allows users to provide and test their own metrics. The package also provides functions for looking at disparity in a serial way (e.g. disparity through time) or per groups as well as visualising the results. Finally, this package provides several statistical tests for disparity analysis.
	"""
	
	homepage = "https://github.com/TGuillerme/dispRity"
	cran = "dispRity" 

	version("1.8", md5="160458928f5e88e16f682085316afb9c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-castor", type=("build", "run"))
	depends_on("r-claddis", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-get", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-phyclust", type=("build", "run"))
	depends_on("r-phylolm", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
