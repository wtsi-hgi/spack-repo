# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUfrisk(RPackage):
	"""Risk Measure Calculation in Financial TS

	Enables the user to calculate Value at Risk (VaR) and Expected 
    Shortfall (ES) by means of various parametric and semiparametric 
    GARCH-type models. For the latter the estimation of the nonparametric scale
    function is carried out by means of a data-driven smoothing approach. Model
    quality, in terms of forecasting VaR and ES, can be assessed by means of 
    various backtesting methods such as the traffic light test for VaR and a 
    newly developed traffic light test for ES. The approaches implemented in 
    this package are described in e.g. Feng Y., Beran J., Letmathe S. and 
    Ghosh S. (2020) <https://ideas.repec.org/p/pdn/ciepap/137.html> as well as 
    Letmathe S., Feng Y. and Uhde A. (2021) 
    <https://ideas.repec.org/p/pdn/ciepap/141.html>. 
	"""
	
	homepage = "https://wiwi.uni-paderborn.de/en/dep4/feng/"
	cran = "ufRisk" 

	version("1.0.7", md5="aeecb60bc658ec251de9ff3c0c4beefe")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-esemifar", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-smoots", type=("build", "run"))
