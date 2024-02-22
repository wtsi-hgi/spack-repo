# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrontier(RPackage):
	"""Stochastic Frontier Analysis

	Maximum Likelihood Estimation of
   Stochastic Frontier Production and Cost Functions.
   Two specifications are available:
   the error components specification with time-varying efficiencies
   (Battese and Coelli, 1992, <doi:10.1007/BF00158774>)
   and a model specification in which the firm effects are directly 
   influenced by a number of variables (Battese and Coelli, 1995,
   <doi:10.1007/BF01205442>).
	"""
	
	homepage = "http://frontier.r-forge.r-project.org/"
	cran = "frontier" 

	version("1.1-8", md5="a8de9311ad4d337d28c6b875bdb263d9")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-micecon@0.6.14:", type=("build", "run"))
	depends_on("r-lmtest@0.9.24:", type=("build", "run"))
	depends_on("r-moments@0.11:", type=("build", "run"))
	depends_on("r-formula@0.2.0:", type=("build", "run"))
	depends_on("r-misctools@0.6.1:", type=("build", "run"))
	depends_on("r-plm@1.0.1:", type=("build", "run"))
