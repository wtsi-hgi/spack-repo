# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLs2wstat(RPackage):
	"""A Multiscale Test of Spatial Stationarity for LS2W Processes

	Wavelet-based methods for testing stationarity and quadtree segmenting of images, see Taylor et al (2014) <doi:10.1080/00401706.2013.823890>.
	"""
	
	cran = "LS2Wstat" 

	version("2.1-5", md5="0dd3c774b1164d0b2fc4fec2071b3129")

	depends_on("r-ls2w@1.3.1:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
