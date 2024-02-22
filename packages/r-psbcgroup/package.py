# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsbcgroup(RPackage):
	"""Penalized Parametric and Semiparametric Bayesian Survival Models
with Shrinkage and Grouping Priors

	Algorithms to implement various Bayesian penalized survival regression models including: semiparametric proportional hazards models with lasso priors (Lee et al., Int J Biostat, 2011 <doi:10.2202/1557-4679.1301>) and three  other shrinkage and group priors (Lee et al., Stat Anal Data Min, 2015 <doi:10.1002/sam.11266>); parametric accelerated failure time models with group/ordinary lasso prior (Lee et al. Comput Stat Data Anal, 2017 <doi:10.1016/j.csda.2017.02.014>).
	"""
	
	cran = "psbcGroup" 

	version("1.7", md5="f0f1aadc5d58d5e7edada72b8c101611")

	depends_on("r-learnbayes", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
