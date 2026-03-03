# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDear(RPackage):
	"""Conventional and Fuzzy Data Envelopment Analysis

	Set of functions for Data Envelopment Analysis. It runs both classic and fuzzy DEA models. See: Banker, R.; Charnes, A.; Cooper, W.W. (1984). <doi:10.1287/mnsc.30.9.1078>, Charnes, A.; Cooper, W.W.; Rhodes, E. (1978). <doi:10.1016/0377-2217(78)90138-8> and Charnes, A.; Cooper, W.W.; Rhodes, E. (1981). <doi:10.1287/mnsc.27.6.668>.
	"""
	
	cran = "deaR" 

	version("1.4.1", md5="7d63f410889292b1ee99c221696b84c4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
