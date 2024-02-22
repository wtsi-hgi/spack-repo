# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdgdetector(RPackage):
	"""Detect SDGs and Targets in Text

	Identify 17 Sustainable Development Goals and associated 169 targets in text.
	"""
	
	homepage = "https://github.com/Yingjie4Science/SDGdetector"
	cran = "SDGdetector" 

	version("2.7.3", md5="f34f69dbb2414585ee5b29f7c0193268")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
