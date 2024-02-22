# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidas2(RPackage):
	"""Bayesian Platform Design with Subgroup Efficacy
Exploration(MIDAS-2)

	The rapid screening of effective and optimal therapies from large numbers of candidate combinations, as well as exploring subgroup efficacy, remains challenging, which necessitates innovative, integrated, and efficient trial designs(Yuan, Y., et al. (2016) <doi:10.1002/sim.6971>). MIDAS-2 package enables quick and continuous screening of promising combination strategies and exploration of their subgroup effects within a unified platform design framework. We used a regression model to characterize the efficacy pattern in subgroups. Information borrowing was applied through Bayesian hierarchical model to improve trial efficiency considering the limited sample size in subgroups(Cunanan, K. M., et al. (2019) <doi:10.1177/1740774518812779>). MIDAS-2 provides an adaptive drug screening and subgroup exploring framework to accelerate immunotherapy development in an efficient, accurate, and integrated fashion(Wathen, J. K., & Thall, P. F. (2017) <doi: 10.1177/1740774517692302>).
	"""
	
	cran = "midas2" 

	version("1.1.0", md5="6ca26763546e0253def3437e5018a993", url="https://cran.r-project.org/src/contrib/midas2_1.1.0.tar.gz")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
