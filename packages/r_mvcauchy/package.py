# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvcauchy(RPackage):
	"""Multivariate Cauchy Distribution

	The Cauchy distribution is a special case of the t distribution when the degrees of freedom are equal to 1. The functions are related to the multivariate Cauchy distribution and include simulation, computation of the density, maximum likelihood estimation, contour plot of the bivariate Cauchy distribution, and discriminant analysis. References include: Nadarajah S. and Kotz S. (2008). "Estimation methods for the multivariate t distribution". Acta Applicandae Mathematicae, 102(1): 99--118. <doi:10.1007/s10440-008-9212-8>, and Kanti V. Mardia, John T. Kent and John M. Bibby (1979). "Multivariate analysis", ISBN:978-0124712522. Academic Press, London.
	"""
	
	cran = "mvcauchy" 

	version("1.0", md5="132d3ca0934082a64bdf2dd3c29f06c6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
