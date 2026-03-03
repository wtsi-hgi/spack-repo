# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCisDglm(RPackage):
	"""Covariates, Interaction, and Selection for DGLM

	An implementation of double generalized linear model (DGLM) building with variable selection procedures and handling of interaction terms and other complex situations. We also provide a method of handling convergence issues within the dglm() function. The package offers a simulation function for generating simulated data for testing purposes and utilizes the forward stepwise variable selection procedure in model-building. It also provides a new custom bootstrap function for mean and standard deviation estimation and functions for building crossplots and squareplots from a data set.
	"""
	
	cran = "CIS.DGLM" 

	version("0.1.0", md5="038c088d4ac87ce61a164c03f84e758b")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dglm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
