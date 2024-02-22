# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInflectssp(RPackage):
	"""Melt Curve Fitting and Melt Shift Analysis

	Analyzes raw abundance data from a cellular thermal shift experiment and calculates melt temperatures and melt shifts for each protein in the experiment. 
    McCracken (2022) <doi:10.1101/2022.12.30.522131>.
	"""
	
	cran = "InflectSSP" 

	version("1.6", md5="f38c900a6458108bcb39405e46ebd3a4")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
