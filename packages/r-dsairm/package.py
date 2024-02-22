# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsairm(RPackage):
	"""Dynamical Systems Approach to Immune Response Modeling

	Simulation models (apps) of various within-host immune response scenarios.
    The purpose of the package is to help individuals learn 
    about within-host infection and immune response modeling from a dynamical systems perspective.
    All apps include explanations of the underlying models and instructions on what to do with the models. 
	"""
	
	homepage = "https://ahgroup.github.io/DSAIRM/"
	cran = "DSAIRM" 

	version("0.9.6", md5="43a5ae55964d8a077d3819351c323f3a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@1.2:", type=("build", "run"))
	depends_on("r-adaptivetau", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
