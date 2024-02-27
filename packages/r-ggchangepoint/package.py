# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgchangepoint(RPackage):
	"""Combines Changepoint Analysis with 'ggplot2'

	R provides fantastic tools for changepoint
    analysis, but plots generated by the tools do 
    not have the 'ggplot2' style. This tool, however, 
    combines 'changepoint', 'changepoint.np' and 'ecp'
    together, and uses 'ggplot2' to visualize changepoints.
	"""
	
	cran = "ggchangepoint" 

	version("0.1.0", md5="455a253992a74a574d96023c55e78772")

	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-changepoint-np", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ecp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))