# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCapm(RPackage):
	"""Companion Animal Population Management

	Quantitative analysis to support companion animal population
    management. Some functions assist survey sampling tasks (calculate sample 
    size for simple and complex designs, select sampling units and estimate 
    population parameters) while others assist the modelling of population 
    dynamics. For demographic characterizations and population management 
    evaluations see: "Baquero, et al." (2018), 
    <doi:10.1016/j.prevetmed.2018.07.006>. For modelling of 
    population dynamics see: "Baquero et al." (2016),
    <doi:10.1016/j.prevetmed.2015.11.009>. For sampling methods
    see: "Levy PS & Lemeshow S" (2013), "ISBN-10: 0470040076"; 
    "Lumley" (2010), "ISBN: 978-0-470-28430-8".
	"""
	
	homepage = "http://oswaldosantos.github.io/capm"
	cran = "capm" 

	version("0.14.0", md5="4119b66bd40ef1225ec91fb25e05ac7b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-fme", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
