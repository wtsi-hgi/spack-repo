# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNiledam(RPackage):
	"""Monazite Dating for the NiLeDAM Team

	Th-U-Pb electron microprobe age dating of monazite, as originally 
             described in <doi:10.1016/0009-2541(96)00024-1>.
	"""
	
	cran = "NiLeDAM" 

	version("0.3", md5="07b588372d1953d33317f1a94f17167d")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-thematic", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
