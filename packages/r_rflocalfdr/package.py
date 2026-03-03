# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRflocalfdr(RPackage):
	"""Significance Level for Random Forest Impurity Importance Scores

	Sets a significance level for  Random Forest MDI (Mean Decrease in Impurity, Gini or
             sum of squares) variable importance scores, using an empirical Bayes approach.
             See Dunne et al. (2022)  <doi:10.1101/2022.04.06.487300>.
	"""
	
	cran = "RFlocalfdr" 

	version("0.8.5", md5="cf40ba0db31461afe3e4a71042cef946")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rflocalfdr-data", type=("build", "run"))
	depends_on("r-vita", type=("build", "run"))
