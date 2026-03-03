# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoxly(RPackage):
	"""Interactive Box Plot

	Interactive box plot using 'plotly' for clinical trial analysis.
	"""
	
	homepage = "https://merck.github.io/boxly/"
	cran = "boxly" 

	version("0.1.1", md5="45f3642172f05401e409ee860a7ba5d6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-metalite", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
