# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimph(RPackage):
	"""Simulate and Plot Estimates from Cox Proportional Hazards Models

	Simulates and plots quantities of interest (relative
    hazards, first differences, and hazard ratios) for linear coefficients,
    multiplicative interactions, polynomials, penalised splines, and
    non-proportional hazards, as well as stratified survival curves from Cox
    Proportional Hazard models. It also simulates and plots marginal effects
    for multiplicative interactions. Methods described in Gandrud (2015)
    <doi:10.18637/jss.v065.i03>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=simPH"
	cran = "simPH" 

	version("1.3.13", md5="caec3b84f7b0fad920ee05d0d7e4c711")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-dplyr@0.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
