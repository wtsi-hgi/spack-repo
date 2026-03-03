# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdiogramfish(RPackage):
	"""Shiny App. Idiograms with Marks and Karyotype Indices

	Plot idiograms of karyotypes, plasmids, circular chr. having a set of data.frames for chromosome data and optionally mark data. Two styles of chromosomes can be used: without or with visible chromatids. Supports micrometers, cM and Mb or any unit. Three styles of centromeres are available: triangle, rounded and inProtein; and six styles of marks are available: square (squareLeft), dots, cM (cMLeft), cenStyle, upArrow (downArrow), exProtein (inProtein); its legend (label) can be drawn inline or to the right of karyotypes. Idiograms can also be plotted in concentric circles. It is possible to calculate chromosome indices by Levan et al. (1964) <doi:10.1111/j.1601-5223.1964.tb01953.x>, karyotype indices of Watanabe et al. (1999) <doi:10.1007/PL00013869> and Romero-Zarco (1986) <doi:10.2307/1221906> and classify chromosomes by morphology Guerra (1986) and Levan et al. (1964).
	"""
	
	homepage = "https://ferroao.gitlab.io/manualidiogramfish/"
	cran = "idiogramFISH" 

	version("2.0.13", md5="31486a970d1df3efc486f6fc03c2e6a5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
