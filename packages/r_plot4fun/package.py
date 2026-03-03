# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlot4fun(RPackage):
	"""Just Plot for Fun

	Explore the world of R graphics with fun and interesting plot functions! 
    Use make_LED() to create dynamic LED screens, draw interconnected rings with Olympic_rings(), 
    and make festive Chinese couplets with chunlian(). 
    Unleash your creativity and turn data into exciting visuals!
	"""
	
	cran = "plot4fun" 

	version("0.1.1", md5="d1c1317bc356310778d320efdc6f7536")
	version("0.1.0", md5="c3c66a7db94c9b9ecab74583fc4d7621")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-pcutils", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-gifski", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
