# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPooling(RPackage):
	"""Fit Poolwise Regression Models

	Functions for calculating power and fitting regression models in studies where a biomarker is measured in "pooled" samples rather than for each individual. Approaches for handling measurement error follow the framework of Schisterman et al. (2010) <doi:10.1002/sim.3823>.
	"""
	
	cran = "pooling" 

	version("1.1.2", md5="40aca008ac52f43f5a95323b6d0a8521")

	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dvmisc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
