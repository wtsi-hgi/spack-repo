# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwi(RPackage):
	"""Count and Continuous Generalized Variability Indexes

	Firstly, both functions of the univariate Poisson dispersion index (DI) for count data and the univariate exponential variation index (VI) for nonnegative continuous data are performed. Next, other functions of univariate indexes such the binomial dispersion index (DIb), the negative binomial dispersion index (DInb) and the inverse Gaussian variation index (VIiG) are given. Finally, we are computed some multivariate versions of these functions such that the generalized dispersion index (GDI) with its marginal one (MDI) and the generalized variation index (GVI) with its marginal one (MVI) too.
	"""
	
	cran = "GWI" 

	version("1.0.2", md5="e2e5d67e8b47717c5f632ddacd2250c3")

