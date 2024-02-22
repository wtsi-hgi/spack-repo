# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdd2ggplot(RPackage):
	"""Add to 'ggplot2'

	Create 'ggplot2' themes and color palettes.
	"""
	
	homepage = "https://github.com/JiaxiangBU/add2ggplot"
	cran = "add2ggplot" 

	version("0.3.0", md5="d86831650b1fcaf60764078e0f83e0b6")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
