# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrigpoints(RPackage):
	"""Data Set of Trig Points in Great Britain in British National
Grid Coordinates

	A complete data set of historic GB trig points in British National Grid (OSGB36) coordinate reference system. Trig points (aka triangulation stations) are fixed survey points used to improve the accuracy of map making in Great Britain during the 20th Century. Trig points are typically located on hilltops so still serve as a useful navigational aid for walkers and hikers today.
	"""
	
	homepage = "https://philmikejones.github.io/trigpoints/"
	cran = "trigpoints" 

	version("1.0.0", md5="6b10e4852efa93e0a75251401610fdcb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
