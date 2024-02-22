# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsqc(RPackage):
	"""Multivariate Statistical Quality Control

	This is a toolkit for multivariate process monitoring. It computes several multivariate control charts e.g. Hotelling, Chi-squared, MEWMA, MCUSUM and Generalized Variance. Ten didactic datasets are included. It also contains some tools for assessing multivariate normality e.g. Mardia's, Royston's and Henze-Zirkler's tests. Please, see the NEWS file for the latest changes in the package.
	"""
	
	homepage = "https://link.springer.com/statistics/computational+statistics/book/978-1-4614-5452-6"
	cran = "MSQC" 

	version("1.1.0", md5="4260f937c4939c7fcc6a045dfc6886e4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
