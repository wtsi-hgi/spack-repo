# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreeks(RPackage):
	"""Sensitivities of Prices of Financial Options and Implied
Volatilities

	Methods to calculate sensitivities of financial option prices for
 European, geometric and arithmetic Asian, and American options, with various
 payoff functions in the Black Scholes model, and in more general jump diffusion
 models. A shiny app to interactively plot the results is included. Furthermore,
 methods to compute implied volatilities are provided for a wide range of option
 types and  custom payoff functions. Classical formulas are implemented for
 European options in the Black Scholes Model, as is presented in Hull, J. C.
 (2017), Options, Futures, and Other Derivatives.
 In the case of Asian options, Malliavin Monte Carlo Greeks are implemented, see
 Hudde, A. & Rüschendorf, L. (2023). European and Asian Greeks for exponential
 Lévy processes. <doi:10.1007/s11009-023-10014-5>. For American
 options, the Binomial Tree  Method is implemented, as is presented in Hull,
 J. C. (2017). 
	"""
	
	cran = "greeks" 

	version("1.3.2", md5="6a92d19fd638f68b7bee6936d691e37d")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
