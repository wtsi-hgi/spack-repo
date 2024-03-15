# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLidr(RPackage):
	"""Airborne LiDAR Data Manipulation and Visualization for Forestry
Applications

	Airborne LiDAR (Light Detection and Ranging) interface for data
    manipulation and visualization. Read/write 'las' and 'laz' files, computation
    of metrics in area based approach, point filtering, artificial point reduction,
    classification from geographic data, normalization, individual tree segmentation
    and other manipulations.
	"""
	
	homepage = "https://github.com/r-lidar/lidR"
	cran = "lidR" 

	version("4.1.1", md5="43e13818a1288dab4b8c1f8abf02fc5f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rlas@1.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-terra@1.5.17:", type=("build", "run"))
	depends_on("r-bh@1.72:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
