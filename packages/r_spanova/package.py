# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpanova(RPackage):
	"""Analysis of Field Trials with Geostatistics & Spatial AR Models

	Perform analysis of variance when the experimental units are spatially correlated. There are two methods to deal with spatial dependence: Spatial autoregressive models (see Rossoni, D. F., & Lima, R. R. (2019) <doi:10.28951/rbb.v37i2.388>) and geostatistics (see Pontes, J. M., & Oliveira, M. S. D. (2004) <doi:10.1590/S1413-70542004000100018>). For both methods, there are three multicomparison procedure available: Tukey, multivariate T, and Scott-Knott.
	"""
	
	cran = "spANOVA" 

	version("0.99.4", md5="022d8b82565c32865614a17789a26c63")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-geor", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-scottknott", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-spatialreg", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
