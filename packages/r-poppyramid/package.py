# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoppyramid(RPackage):
	"""Population Pyramids

	Functions that facilitate the elaboration of population pyramids.  
	"""
	
	homepage = "https://github.com/musajajorge/popPyramid"
	cran = "popPyramid" 

	version("0.1.1", md5="80b0de2ed8df201bde72823a96e443e7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
