# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlive(RPackage):
	"""Automated Estimation of Sigmoidal and Piecewise Linear Mixed
Models

	Estimation of relatively complex nonlinear mixed-effects models, including the Sigmoidal Mixed Model and the Piecewise Linear Mixed Model with abrupt or smooth transition, through a single intuitive line of code and with automated generation of starting values. 
	"""
	
	homepage = "https://github.com/MaudeWagner/nlive"
	cran = "nlive" 

	version("0.2.0", md5="1bc7ba1d0646f11b78867af0f84fa0f0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nlraa", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lcmm", type=("build", "run"))
	depends_on("r-saemix", type=("build", "run"))
	depends_on("r-rmisc", type=("build", "run"))
	depends_on("r-sitar", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
