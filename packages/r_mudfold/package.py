# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMudfold(RPackage):
	"""Multiple UniDimensional unFOLDing

	Nonparametric unfolding item response theory (IRT) model for dichotomous data (see W.H. Van Schuur (1984). Structure in Political Beliefs: A New Model for Stochastic Unfolding with Application to European Party Activists, and W.J.Post (1992). Nonparametric Unfolding Models: A Latent Structure Approach). The package implements MUDFOLD (Multiple UniDimensional unFOLDing), an iterative item selection algorithm that constructs unfolding scales from dichotomous preferential-choice data without explicitly assuming a parametric form of the item response functions. Scale diagnostics from Post(1992) and estimates for the person locations proposed by Johnson(2006) and Van Schuur(1984) are also available. This model can be seen as the unfolding variant of Mokken(1971) scaling method.
	"""
	
	homepage = "https://github.com/cran/mudfold"
	cran = "mudfold" 

	version("1.1.21", md5="3a92793517da1368ce57c47be5586373")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
