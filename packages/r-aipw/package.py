# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAipw(RPackage):
	"""Augmented Inverse Probability Weighting

	The 'AIPW' pacakge implements the augmented inverse probability weighting, a doubly robust estimator, for average causal effect estimation with user-defined stacked machine learning algorithms. To cite the 'AIPW' package, please use: "Yongqi Zhong, Edward H. Kennedy, Lisa M. Bodnar, Ashley I. Naimi (2021, In Press). AIPW: An R Package for Augmented Inverse Probability Weighted Estimation of Average Causal Effects. American Journal of Epidemiology". Visit: <https://yqzhong7.github.io/AIPW/> for more information.
	"""
	
	homepage = "https://github.com/yqzhong7/AIPW"
	cran = "AIPW" 

	version("0.6.3.2", md5="7e59d8a4881fd6d9f3173f607e973b45")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
