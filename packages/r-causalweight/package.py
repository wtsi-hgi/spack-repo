# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalweight(RPackage):
	"""Estimation Methods for Causal Inference Based on Inverse
Probability Weighting

	Various estimators of causal effects based on inverse probability weighting, doubly robust estimation, and double machine learning. Specifically, the package includes methods for estimating average treatment effects, direct and indirect effects in causal mediation analysis, and dynamic treatment effects. The models refer to studies of Froelich (2007) <doi:10.1016/j.jeconom.2006.06.004>, Huber (2012) <doi:10.3102/1076998611411917>, Huber (2014) <doi:10.1080/07474938.2013.806197>, Huber (2014) <doi:10.1002/jae.2341>, Froelich and Huber (2017) <doi:10.1111/rssb.12232>, Hsu, Huber, Lee, and Lettry (2020)  <doi:10.1002/jae.2765>, and others.
	"""
	
	cran = "causalweight" 

	version("1.1.0", md5="fbd94d35ce1717c50a87836872adb8c8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-larf", type=("build", "run"))
	depends_on("r-hdm", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-grf", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
