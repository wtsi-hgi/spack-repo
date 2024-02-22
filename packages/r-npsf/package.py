# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpsf(RPackage):
	"""Nonparametric and Stochastic Efficiency and Productivity
Analysis

	Nonparametric efficiency measurement and statistical inference via DEA type estimators (see Färe, Grosskopf, and Lovell (1994) <doi:10.1017/CBO9780511551710>, Kneip, Simar, and Wilson (2008) <doi:10.1017/S0266466608080651> and Badunenko and Mozharovskyi (2020) <doi:10.1080/01605682.2019.1599778>) as well as Stochastic Frontier estimators for both cross-sectional data and 1st, 2nd, and 4th generation models for panel data (see Kumbhakar and Lovell (2003) <doi:10.1017/CBO9781139174411>, Badunenko and Kumbhakar (2016) <doi:10.1016/j.ejor.2016.04.049>). The stochastic frontier estimators can handle both half-normal and truncated normal models with conditional mean and heteroskedasticity. The marginal effects of determinants can be obtained.
	"""
	
	cran = "npsf" 

	version("0.8.0", md5="8bf6fc3428ed1e539a2d76a6e456886a")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
