# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeibullrLearnr(RPackage):
	"""An Interactive Introduction to Life Data Analysis

	An interactive introduction to Life Data Analysis that depends on 'WeibullR' 
  by David Silkworth and Jurgen Symynck (2022) <https://CRAN.R-project.org/package=WeibullR>, 
  a R package for Weibull Analysis, and 'learnr' by Garrick Aden-Buie et al. (2023) 
  <https://CRAN.R-project.org/package=learnr>, a framework for building interactive learning 
  modules in R. 
	"""
	
	homepage = "https://paulgovan.github.io/WeibullR.learnr/"
	cran = "WeibullR.learnr" 

	version("0.1.1", md5="18e67af15dc1835f2529a3a22b72d3a6")

	depends_on("r-learnr", type=("build", "run"))
	depends_on("r-weibullr", type=("build", "run"))
