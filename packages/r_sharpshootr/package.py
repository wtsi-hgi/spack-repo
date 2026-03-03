# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharpshootr(RPackage):
	"""A Soil Survey Toolkit

	Miscellaneous soil data management, summary, visualization, and conversion utilities to support soil survey.
	"""
	
	homepage = "https://github.com/ncss-tech/sharpshootR"
	cran = "sharpshootR" 

	version("2.2", md5="a0947411738291f221ef9c2db7f81d6d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-aqp", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-soildb", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
