# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvidm(RPackage):
	"""Inference and Prediction in an Illness-Death Model

	Newly developed methods for the estimation of several probabilities
      in an illness-death model. The package can be used to obtain nonparametric and 
      semiparametric estimates for: transition probabilities, occupation probabilities, 
      cumulative incidence function and the sojourn time distributions. 
      Additionally, it is possible to fit proportional hazards regression models
      in each transition of the Illness-Death Model. Several auxiliary 
      functions are also provided which can be used for marginal 
      estimation of the survival functions.
	"""
	
	cran = "survidm" 

	version("1.3.2", md5="eaadc474d5251150b08c604f0349d72e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-tpmsm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
