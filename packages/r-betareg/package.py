# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetareg(RPackage):
	"""Beta Regression

	Beta regression for modeling beta-distributed dependent variables, e.g., rates and proportions.
  In addition to maximum likelihood regression (for both mean and precision of a beta-distributed
  response), bias-corrected and bias-reduced estimation as well as finite mixture models and
  recursive partitioning for beta regressions are provided.
	"""
	
	cran = "betareg" 

	version("3.1-4", md5="bd810dfc3c20c7b8c7ac858198e1cb5b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
