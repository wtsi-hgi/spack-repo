# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcessmapr(RPackage):
	"""Construct Process Maps Using Event Data

	Visualize event logs using directed graphs, i.e. process maps. Part of the 'bupaR' framework.
	"""
	
	homepage = "https://bupar.net/"
	cran = "processmapR" 

	version("0.5.3", md5="8ecb6835da319680befaec327cfe18b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-bupar@0.5.1:", type=("build", "run"))
	depends_on("r-edear@0.9:", type=("build", "run"))
	depends_on("r-diagrammer@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
