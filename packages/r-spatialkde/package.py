# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialkde(RPackage):
	"""Kernel Density Estimation for Spatial Data

	Calculate Kernel Density Estimation (KDE) for spatial data. 
  The algorithm is inspired by the tool 'Heatmap' from 'QGIS'. The method is described by:
  Hart, T., Zandbergen, P. (2014) <doi:10.1108/PIJPSM-04-2013-0039>, 
  Nelson, T. A., Boots, B. (2008) <doi:10.1111/j.0906-7590.2008.05548.x>,
  Chainey, S., Tompson, L., Uhlig, S.(2008) <doi:10.1057/palgrave.sj.8350066>.
	"""
	
	homepage = "https://jancaha.github.io/SpatialKDE/index.html"
	cran = "SpatialKDE" 

	version("0.8.2", md5="09ff8439a0e3f88887f11a5eda7389b3")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
