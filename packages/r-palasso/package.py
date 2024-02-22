# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalasso(RPackage):
	"""Paired Lasso Regression

	Implements sparse regression with paired covariates (Rauschenberger et al. 2020 <doi:10.1007/s11634-019-00375-6>). For the optional shrinkage, install ashr (<https://github.com/stephens999/ashr>) and CorShrink (<https://github.com/kkdey/CorShrink>) from GitHub (see README).
	"""
	
	homepage = "https://github.com/rauschenberger/palasso"
	cran = "palasso" 

	version("0.0.9", md5="97eebafa367d2838d3fc1023aeb20bb5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
