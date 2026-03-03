# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLive(RPackage):
	"""Local Interpretable (Model-Agnostic) Visual Explanations

	Interpretability of complex machine learning models is a growing concern.
    This package helps to understand key factors that drive the 
    decision made by complicated predictive model (so called black box model). 
    This is achieved through local approximations that are either based on 
    additive regression like model or CART like model that allows for 
    higher interactions. The methodology is based on Tulio Ribeiro, Singh, Guestrin (2016) <doi:10.1145/2939672.2939778>.
    More details can be found in Staniak, Biecek (2018) <doi:10.32614/RJ-2018-072>.
	"""
	
	homepage = "https://github.com/ModelOriented/live"
	cran = "live" 

	version("1.5.13", md5="d1478c22c5e51754d65c479f5e96fb83")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mlr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-breakdown", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-forestmodel", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gower", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
