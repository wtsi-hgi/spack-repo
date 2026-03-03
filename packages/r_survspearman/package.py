# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvspearman(RPackage):
	"""Nonparametric Spearman's Correlation for Survival Data

	Nonparametric estimation of Spearman's rank correlation with bivariate survival (right-censored) data as described in Eden, S.K., Li, C., Shepherd B.E. (2021), Nonparametric Estimation of Spearman's Rank Correlation with Bivariate Survival Data, Biometrics (under revision). The package also provides functions that visualize bivariate survival data and bivariate probability mass function.
	"""
	
	cran = "survSpearman" 

	version("1.0.1", md5="2199e2b1b79ee4f89ddc9ec5944f9277")

	depends_on("r@3.5:", type=("build", "run"))
