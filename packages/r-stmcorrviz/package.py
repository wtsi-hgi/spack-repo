# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStmcorrviz(RPackage):
	"""A Tool for Structural Topic Model Visualizations

	Generates an interactive visualization of topic correlations/
    hierarchy in a Structural Topic Model (STM) of Roberts, Stewart, and Tingley.
    The package performs a hierarchical clustering of topics which are then exported
    to a JSON object and visualized using D3.
	"""
	
	cran = "stmCorrViz" 

	version("1.3", md5="ba8d2f716b76aaf5d85abb90fdaff972")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stm", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
