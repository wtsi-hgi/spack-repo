# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopodistance(RPackage):
	"""Calculating Topographic Paths and Distances

	A toolkit for calculating topographic distances and identifying and plotting topographic paths. Topographic distances can be calculated along shortest topographic paths (Wang (2009) <doi:10.1111/j.1365-294X.2009.04338.x>), weighted topographic paths (Zhan et al. (1993) <doi:10.1007/3-540-57207-4_29>), and topographic least cost paths (Wang and Summers (2010) <doi:10.1111/j.1365-294X.2009.04465.x>). Functions can map topographic paths on colored or hill shade maps and plot topographic cross sections (elevation profiles) for the paths.
	"""
	
	cran = "topoDistance" 

	version("1.0.2", md5="d8a5334f36701efe51a559ab9cac8804")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
