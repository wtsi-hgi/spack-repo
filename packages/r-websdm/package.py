# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebsdm(RPackage):
	"""Including Known Interactions in Species Distribution Models

	A collection of tools to fit and work with trophic Species Distribution Models. Trophic Species Distribution Models combine knowledge of trophic interactions with Bayesian structural equation models that model each species as a function of its prey (or predators) and environmental conditions. It exploits the topological ordering of the known trophic interaction network to predict species distribution in space and/or time, where the prey (or predator) distribution is unavailable. The method implemented by the package is described in Poggiato, Andréoletti, Pollock and Thuiller (2022) <doi:10.22541/au.166853394.45823739/v1>.
	"""
	
	homepage = "https://github.com/giopogg/webSDM"
	cran = "webSDM" 

	version("1.1-4", md5="3609a09fd91fe53ea11f15fba493cc27")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-dismo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-jtools", type=("build", "run"))
	depends_on("r-rstanarm", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
