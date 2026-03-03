# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGic(RPackage):
	"""A General Iterative Clustering Algorithm

	An iterative algorithm that improves the proximity matrix (PM) from a random forest (RF) and the resulting clusters as measured by the silhouette score.
	"""
	
	cran = "GIC" 

	version("1.0.0", md5="1444601882630b8dff17714c2c914bd6")

	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
