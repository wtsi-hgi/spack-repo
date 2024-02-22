# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfocus(RPackage):
	"""Scales that Focus Specific Levels in your ggplot()

	A 'ggplot2' extension that provides tools for automatically
    creating scales to focus on subgroups of the data plotted 
    without losing other information.
	"""
	
	homepage = "https://github.com/Freguglia/ggfocus"
	cran = "ggfocus" 

	version("1.0.0", md5="82318000cf24087298351ddf45cda499")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
