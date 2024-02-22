# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobmixreg(RPackage):
	"""Robust Mixture Regression

	Finite mixture models are a popular technique for modelling unobserved heterogeneity or to approximate general distribution functions in a semi-parametric way. They are used in a lot of different areas such as astronomy, biology, economics, marketing or medicine.
             This package is the implementation of popular robust mixture regression methods based on different algorithms including: fleximix, finite mixture models and latent class regression; CTLERob, component-wise adaptive trimming likelihood estimation; mixbi, bi-square estimation; mixL, Laplacian distribution; mixt, t-distribution; TLE, trimmed likelihood estimation.
             The implemented algorithms includes:  CTLERob stands for Component-wise adaptive Trimming Likelihood Estimation based mixture regression; mixbi stands for mixture regression based on bi-square estimation; mixLstands for mixture regression based on Laplacian distribution; TLE stands for Trimmed Likelihood Estimation based mixture regression. For more detail of the algorithms, please refer to below references. 
             Reference: Chun Yu, Weixin Yao, Kun Chen (2017) <doi:10.1002/cjs.11310>.
             NeyKov N, Filzmoser P, Dimova R et al. (2007) <doi:10.1016/j.csda.2006.12.024>.
             Bai X, Yao W. Boyer JE (2012) <doi:10.1016/j.csda.2012.01.016>.
             Wennan Chang, Xinyu Zhou, Yong Zang, Chi Zhang, Sha Cao (2020) <arXiv:2005.11599>.
	"""
	
	homepage = "https://changwn.github.io/RobMixReg/"
	cran = "RobMixReg" 

	version("1.1.0", md5="1b56a9b8de2dc7bcf27b6cb149586f67")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-robust", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
