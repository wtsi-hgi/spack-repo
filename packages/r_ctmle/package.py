# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtmle(RPackage):
	"""Collaborative Targeted Maximum Likelihood Estimation

	Implements the general template for collaborative targeted maximum likelihood estimation. It also provides several commonly used C-TMLE instantiation, like the vanilla/scalable variable-selection C-TMLE (Ju et al. (2017) <doi:10.1177/0962280217729845>) and the glmnet-C-TMLE algorithm (Ju et al. (2017) <arXiv:1706.10029>). 
	"""
	
	cran = "ctmle" 

	version("0.1.2", md5="607d771b8bfbd8fd099958dc4d884cb8")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-tmle", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
