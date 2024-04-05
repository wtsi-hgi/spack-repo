# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArm(RPackage):
	"""Data Analysis Using Regression and Multilevel/Hierarchical
Models

	Functions to accompany A. Gelman and J. Hill, Data Analysis Using Regression and Multilevel/Hierarchical Models, Cambridge University Press, 2007.
	"""
	
	homepage = "https://CRAN.R-project.org/package=arm"
	cran = "arm" 

	version("1.14-4", md5="7a901ecf306d25cb94228a4bc03bc050")
	version("1.13-1", md5="45f20b21de61f2132e7ba652d52ff36d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1:", type=("build", "run"))
	depends_on("r-lme4@1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
