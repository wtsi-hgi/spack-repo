# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApis(RPackage):
	"""Auto-Adaptive Parentage Inference Software Tolerant to Missing
Parents

	Parentage assignment package.
    Parentage assignment is performed based on observed average Mendelian transmission probability distributions or Exclusion.
    The main functions of this package are the function APIS_2n(), APIS_3n and launch_APIShiny(), which perform parentage assignment.
	"""
	
	cran = "APIS" 

	version("2.0.4", md5="285a11de85312d35196422c7ecbf03ba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
