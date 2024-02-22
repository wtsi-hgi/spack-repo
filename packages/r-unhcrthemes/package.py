# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnhcrthemes(RPackage):
	"""UNHCR 'ggplot2' Theme and Colour Palettes

	A 'ggplot2' theme and color palettes following
    the United Nations High Commissioner for Refugees (UNHCR) Data Visualization Guidelines recommendations.
	"""
	
	homepage = "https://github.com/unhcr-dataviz/unhcrthemes"
	cran = "unhcrthemes" 

	version("0.6.2", md5="e105dfd1272b31018534af9458723c8b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-systemfonts", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
