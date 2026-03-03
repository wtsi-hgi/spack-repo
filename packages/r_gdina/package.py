# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdina(RPackage):
	"""The Generalized DINA Model Framework

	A set of psychometric tools for cognitive diagnosis modeling based on the generalized deterministic inputs, noisy and gate (G-DINA) model by de la Torre (2011) <DOI:10.1007/s11336-011-9207-7> and its extensions, including the sequential G-DINA model by Ma and de la Torre (2016) <DOI:10.1111/bmsp.12070> for polytomous responses, and the polytomous G-DINA model by Chen and de la Torre <DOI:10.1177/0146621613479818> for polytomous attributes. Joint attribute distribution can be independent, saturated, higher-order, loglinear smoothed or structured. Q-matrix validation, item and model fit statistics, model comparison at test and item level and differential item functioning can also be conducted. A graphical user interface is also provided. For tutorials, please check Ma and de la Torre (2020) <DOI:10.18637/jss.v093.i14>, Ma and de la Torre (2019) <DOI:10.1111/emip.12262>, Ma (2019) <DOI:10.1007/978-3-030-05584-4_29> and de la Torre and Akbay (2019). 
	"""
	
	homepage = "https://github.com/Wenchao-Ma/GDINA"
	cran = "GDINA" 

	version("2.9.4", md5="8bd884d5f6fbb2d6596d27987d89d2ea")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
