# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvaluefunctions(RPackage):
	"""Creates and Plots P-Value Functions, S-Value Functions,
Confidence Distributions and Confidence Densities

	Contains functions to compute and plot confidence distributions, confidence densities, p-value functions and s-value (surprisal) functions for several commonly used estimates. Instead of just calculating one p-value and one confidence interval, p-value functions display p-values and confidence intervals for many levels thereby allowing to gauge the compatibility of several parameter values with the data. These methods are discussed by Infanger D, Schmidt-Trucksäss A. (2019) <doi:10.1002/sim.8293>; Poole C. (1987) <doi:10.2105/AJPH.77.2.195>; Schweder T, Hjort NL. (2002) <doi:10.1111/1467-9469.00285>; Bender R, Berg G, Zeeb H. (2005) <doi:10.1002/bimj.200410104> ; Singh K, Xie M, Strawderman WE. (2007) <doi:10.1214/074921707000000102>; Rothman KJ, Greenland S, Lash TL. (2008, ISBN:9781451190052); Amrhein V, Trafimow D, Greenland S. (2019) <doi:10.1080/00031305.2018.1543137>; Greenland S. (2019) <doi:10.1080/00031305.2018.1529625> and Rafi Z, Greenland S. (2020) <doi:10.1186/s12874-020-01105-9>.
	"""
	
	homepage = "https://github.com/DInfanger/pvaluefunctions"
	cran = "pvaluefunctions" 

	version("1.6.2", md5="f462b0209e4f5ecddeb275fe9e1d2b50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-zipfr@0.6.70:", type=("build", "run"))
	depends_on("r-pracma@2.3.3:", type=("build", "run"))
	depends_on("r-gsl@2.1.7.1:", type=("build", "run"))
