# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopularemada(RPackage):
	"""Copula Mixed Models for Multivariate Meta-Analysis of Diagnostic
Test Accuracy Studies

	The bivariate copula mixed model for meta-analysis of diagnostic test accuracy studies in Nikoloulopoulos (2015) <doi:10.1002/sim.6595>. The vine copula mixed model for meta-analysis of diagnostic test accuracy studies accounting for disease prevalence in Nikoloulopoulos (2017) <doi:10.1177/0962280215596769> and also accounting for non-evaluable subjects in Nikoloulopoulos (2020) <doi:10.1515/ijb-2019-0107>. The hybrid vine copula mixed model for meta-analysis of diagnostic test accuracy case-control and cohort studies in Nikoloulopoulos (2018) <doi:10.1177/0962280216682376>. The D-vine copula mixed model for meta-analysis and comparison of two diagnostic tests in Nikoloulopoulos (2019) <doi:10.1177/0962280218796685>. The multinomial quadrivariate D-vine copula mixed model for meta-analysis of diagnostic tests with non-evaluable subjects in Nikoloulopoulos (2020) <doi:10.1177/0962280220913898>. The one-factor copula mixed model for joint meta-analysis of multiple diagnostic tests (2022) <doi:10.1111/rssa.12838>. 
	"""
	
	cran = "CopulaREMADA" 

	version("1.5.1", md5="516c1578b40ace6d4520f06655c50398")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
