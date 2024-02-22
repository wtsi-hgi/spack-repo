# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmeta(RPackage):
	"""Multivariate Meta-Analysis

	Multiple 2 by 2 tables often arise in meta-analysis which combines statistical evidence from multiple studies. Two risks within the same study are possibly correlated because they share some common factors such as environment and population structure. This package implements a set of novel Bayesian approaches for multivariate meta analysis when the risks within the same study are independent or correlated. The exact posterior inference of odds ratio, relative risk, and risk difference given either a single 2 by 2 table or multiple 2 by 2 tables is provided. Luo, Chen, Su, Chu, (2014) <doi:10.18637/jss.v056.i11>, Chen, Luo, (2011) <doi:10.1002/sim.4248>, Chen, Chu, Luo, Nie, Chen, (2015) <doi:10.1177/0962280211430889>, Chen, Luo, Chu, Su, Nie, (2014) <doi:10.1080/03610926.2012.700379>, Chen, Luo, Chu, Wei, (2013) <doi:10.1080/19466315.2013.791483>.
	"""
	
	cran = "mmeta" 

	version("3.0.0", md5="f733816c4bdc1926973cc88c765cbf35")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
