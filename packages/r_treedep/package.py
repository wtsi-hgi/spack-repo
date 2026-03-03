# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreedep(RPackage):
	"""Air Pollution Removal by Dry Deposition on Trees

	The model estimates air pollution removal by dry deposition on trees. It also estimates or uses hourly values for aerodynamic resistance, boundary layer resistance, canopy resistance, stomatal resistance, cuticular resistance, mesophyll resistance, soil resistance, friction velocity and deposition velocity. It also allows plotting graphical results for a specific time period. The pollutants are nitrogen dioxide, ozone, sulphur dioxide, carbon monoxide and particulate matter. Baldocchi D (1994) <doi:10.1093/treephys/14.7-8-9.1069>. Farquhar GD, von Caemmerer S, Berry JA (1980) Planta 149: 78-90. Hirabayashi S, Kroll CN, Nowak DJ (2015) i-Tree Eco Dry Deposition Model. Nowak DJ, Crane DE, Stevens JC (2006) <doi:10.1016/j.ufug.2006.01.007>. US EPA (1999) PCRAMMET User's Guide. EPA-454/B-96-001. Weiss A, Norman JM (1985) Agricultural and Forest Meteorology 34: 205—213.
	"""
	
	cran = "TreeDep" 

	version("0.1.3", md5="5331adefbc57cd6524ba81f4aff734b5")

	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
