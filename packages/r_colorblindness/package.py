# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorblindness(RPackage):
	"""Safe Color Set for Color Blindness

	Provide the safe color set for color blindness, 
         the simulator of protanopia, deuteranopia.
         The color sets are collected from:
         Wong, B. (2011) <doi:10.1038/nmeth.1618>, and
         <http://mkweb.bcgsc.ca/biovis2012/>.
         The simulations of the appearance of the colors to color-deficient
         viewers were based on algorithms in
         Vienot, F., Brettel, H. and Mollon, J.D. (1999) 
         <doi:10.1002/(SICI)1520-6378(199908)24:4%3C243::AID-COL5%3E3.0.CO;2-3>.
         The cvdPlot() function to generate 'ggplot' grobs of simulations 
         were modified from <https://github.com/clauswilke/colorblindr>.
	"""
	
	cran = "colorBlindness" 

	version("0.1.9", md5="8137dac86e31e01daa7a7f42296376d9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-gridgraphics", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
