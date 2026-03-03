# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROenokpm(RPackage):
	"""Modeling the Kinetics of Carbon Dioxide Production in Alcoholic
Fermentation

	Developed to help researchers who need to model the kinetics of carbon dioxide (CO2) production in alcoholic fermentation of wines, beers and other fermented products. The following models are available for modeling the carbon dioxide production curve as a function of time: 5PL, Gompertz and 4PL. This package has different functions, which applied can: perform the modeling of the data obtained in the fermentation and return the coefficients, analyze the model fit and return different statistical metrics, and calculate the kinetic parameters: Maximum production of carbon dioxide; Maximum rate of production of carbon dioxide; Moment in which maximum fermentation rate occurs; Duration of the latency phase for carbon dioxide production; Carbon dioxide produced until maximum fermentation rate occurs. In addition, a function that generates graphs with the observed and predicted data from the models, isolated and combined, is available. Gava, A., Borsato, D., & Ficagna, E. (2020)."Effect of mixture of fining agents on the fermentation kinetics of base wine for sparkling wine production: Use of methodology for modeling". <doi:10.1016/j.lwt.2020.109660>.
	"""
	
	cran = "OenoKPM" 

	version("2.2.1", md5="0b84368d1dbfe5acafcf0c74ed8f40f3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
