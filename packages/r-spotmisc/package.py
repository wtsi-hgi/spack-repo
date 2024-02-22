# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpotmisc(RPackage):
	"""Misc Extensions for the 'SPOT' Package

	Implements additional models, simulation tools, and interfaces as extensions to 'SPOT'.
    It provides tools for hyperparameter tuning via 'keras/tensorflow', interfacing 'mlr', for performing Markov chain simulations, 
    and for sensitivity analysis based on sequential bifurcation methods as described in Bettonvil and Kleijnen (1996). 
    Furthermore, additional plotting functions for output from 'SPOT' runs are implemented.
    Bartz-Beielstein T, Lasarczyk C W G, Preuss M (2005) <doi:10.1109/CEC.2005.1554761>.
    Bartz-Beielstein T, Zaefferer M, Rehbach F (2021) <arXiv:1712.04076>.
    Bartz-Beielstein T, Rehbach F, Sen A, Zaefferer M <arXiv:2105.14625>.
    Bettonvil, B, Kleijnen JPC (1996) <doi:10.1016/S0377-2217(96)00156-7>.
	"""
	
	homepage = "https://www.spotseven.de"
	cran = "SPOTMisc" 

	version("1.19.52", md5="620c6f3a1cd83f8631324a51eb905f4d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mlr", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-sensitivity", type=("build", "run"))
	depends_on("r-smoof", type=("build", "run"))
	depends_on("r-spot", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-tfdatasets", type=("build", "run"))
