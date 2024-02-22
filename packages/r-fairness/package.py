# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFairness(RPackage):
	"""Algorithmic Fairness Metrics

	Offers calculation, visualization and comparison of algorithmic fairness metrics. Fair machine learning is an emerging topic with the overarching aim to critically assess whether ML algorithms reinforce existing social biases. Unfair algorithms can propagate such biases and produce predictions with a disparate impact on various sensitive groups of individuals (defined by sex, gender, ethnicity, religion, income, socioeconomic status, physical or mental disabilities). Fair algorithms possess the underlying foundation that these groups should be treated similarly or have similar prediction outcomes. The fairness R package offers the calculation and comparisons of commonly and less commonly used fairness metrics in population subgroups. These methods are described by Calders and Verwer (2010) <doi:10.1007/s10618-010-0190-x>, Chouldechova (2017) <doi:10.1089/big.2016.0047>, Feldman et al. (2015) <doi:10.1145/2783258.2783311> , Friedler et al. (2018) <doi:10.1145/3287560.3287589> and Zafar et al. (2017) <doi:10.1145/3038912.3052660>. The package also offers convenient visualizations to help understand fairness metrics.
	"""
	
	homepage = "https://kozodoi.me/r/fairness/packages/2020/05/01/fairness-tutorial.html"
	cran = "fairness" 

	version("1.2.2", md5="9d76842530b3f2d04109786bfee2a333")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
