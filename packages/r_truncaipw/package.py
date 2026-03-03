# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTruncaipw(RPackage):
	"""Doubly Robust Estimation under Covariate-Induced Dependent Left
Truncation

	Doubly robust estimation for the mean of an arbitrarily transformed survival time under covariate-induced dependent left truncation and noninformative right censoring. The functions truncAIPW(), truncAIPW_cen1(), and truncAIPW_cen2() compute the doubly robust estimators under the scenario without censoring and the two censoring scenarios, respectively. The package also contains three simulated data sets 'simu', 'simu_c1', and 'simu_c2', which are used to illustrate the usage of the functions in this package.
    Reference: Wang, Y., Ying, A., Xu, R. (2022) "Doubly robust estimation under covariate-induced dependent left truncation" <arXiv:2208.06836>.
	"""
	
	homepage = "https://arxiv.org/pdf/2208.06836.pdf"
	cran = "truncAIPW" 

	version("1.0.1", md5="c9c5d0ceb24802707d76cf9ca0164527")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survpen", type=("build", "run"))
