# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuiplot(RPackage):
	"""User-Friendly GUI Plotting Tools

	Create a user-friendly plotting GUI for 'R'.
    In addition, one purpose of creating the 'R' package is to facilitate third-party software to call 'R' for drawing, for example, 'Phoenix WinNonlin' software calls 'R' to draw the drug concentration versus time curve.
	"""
	
	homepage = "https://s0521.github.io/guiplot/about/"
	cran = "guiplot" 

	version("0.5.0", md5="55106bf7f73dc57c3abfb31520f08a03")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-excelr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
