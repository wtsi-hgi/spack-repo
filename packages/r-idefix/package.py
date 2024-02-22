# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdefix(RPackage):
	"""Efficient Designs for Discrete Choice Experiments

	Generates efficient designs for discrete choice experiments based on the multinomial logit model, and individually adapted designs for the mixed multinomial logit model. The generated designs can be presented on screen and choice data can be gathered using a shiny application. Traets F, Sanchez G, and Vandebroek M (2020) <doi:10.18637/jss.v096.i03>.
	"""
	
	homepage = "https://github.com/traets/idefix"
	cran = "idefix" 

	version("1.0.3", md5="24fafff62b405ab26f4992aee1b6e3b8")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-dfidx", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
