# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpotoroo(RPackage):
	"""Spatiotemporal Clustering of Satellite Hot Spot Data

	An algorithm to cluster satellite hot spot data spatially and temporally.
	"""
	
	homepage = "https://tengmcing.github.io/spotoroo/"
	cran = "spotoroo" 

	version("0.1.4", md5="a017f681accc038da3e8a9a9d9e7e2e8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-geodist@0.0.4:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-cli@2.3:", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggextra@0.9:", type=("build", "run"))
	depends_on("r-ggbeeswarm@0.7.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
