# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForesttools(RPackage):
	"""Tools for Analyzing Remote Sensing Forest Data

	Tools for analyzing remote sensing forest data, including functions for detecting treetops from canopy models, outlining tree crowns, and calculating textural metrics.
	"""
	
	homepage = "https://github.com/andrew-plowright/ForestTools"
	cran = "ForestTools" 

	version("1.0.1", md5="4fa6fa3af18a668aee6624f3cf2d7805")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
