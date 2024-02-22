# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlcare(RPackage):
	"""Semiparametric Latent Class Analysis of Recurrent Events

	Efficient R package for latent class analysis of recurrent events, based on the semiparametric multiplicative intensity model by Zhao et al. (2022) <doi:10.1111/rssb.12499>. SLCARE returns estimates for non-functional model parameters along with the associated variance estimates and p-values. Visualization tools are provided to depict the estimated functional model parameters and related functional quantities of interest. SLCARE also delivers a model checking plot to help assess the adequacy of the fitted model.
	"""
	
	cran = "SLCARE" 

	version("1.1.0", md5="519f076a5b20094a0e4cf512c95edf26")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-reda", type=("build", "run"))
	depends_on("r-rereg", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
