# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulaSurv(RPackage):
	"""Analysis of Bivariate Survival Data Based on Copulas

	Simulating bivariate survival data from copula models.
 Estimation of the association parameter in copula models.
 Two different ways to estimate the association parameter in copula models are implemented.
 A goodness-of-fit test for a given copula model is implemented.
 See Emura, Lin and Wang (2010) <doi:10.1016/j.csda.2010.03.013> for details.
	"""
	
	cran = "Copula.surv" 

	version("1.4", md5="477604fe702e31f02ee303ae98841319")

