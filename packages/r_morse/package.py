# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorse(RPackage):
	"""Modelling Reproduction and Survival Data in Ecotoxicology

	Advanced methods for a valuable quantitative environmental risk 
   assessment using Bayesian inference of survival and reproduction Data. Among
   others, it facilitates Bayesian inference of the general unified
   threshold model of survival (GUTS). See our companion paper 
   Baudrot and Charles (2021) <doi:10.21105/joss.03200>,
   as well as complementary details in Baudrot et al. (2018)
   <doi:10.1021/acs.est.7b05464> and Delignette-Muller et al.
   (2017) <doi:10.1021/acs.est.6b05326>.
	"""
	
	homepage = "https://cran.r-project.org/package=morse"
	cran = "morse" 

	version("3.3.2", md5="86407de068ca11acd3fbb62a6936cf24")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rjags@4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("jags@4.0.0:", type=("build", "link", "run"))
