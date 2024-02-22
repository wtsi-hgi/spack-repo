# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoefplot(RPackage):
	"""Plots Coefficients from Fitted Models

	Plots the coefficients from model objects. This very quickly shows the user the point estimates and confidence intervals for fitted models.
	"""
	
	cran = "coefplot" 

	version("1.2.8", md5="17690ba08f76e0b6e722610f9a34f3bf")

	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-useful", type=("build", "run"))
	depends_on("r-dplyr@0.6:", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
