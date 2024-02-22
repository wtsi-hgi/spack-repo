# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBivpois(RPackage):
	"""Bivariate Poisson Distribution

	Maximum likelihood estimation, random values generation, density computation and other functions for the bivariate Poisson distribution. References include: Kawamura K. (1984). "Direct calculation of maximum likelihood estimator for the bivariate Poisson distribution". Kodai Mathematical Journal, 7(2): 211--221. <doi:10.2996/kmj/1138036908>. Kocherlakota S. and Kocherlakota K. (1992). "Bivariate discrete distributions". CRC Press. <doi:10.1201/9781315138480>. Karlis D. and Ntzoufras I. (2003). "Analysis of sports data by using bivariate Poisson models". Journal of the Royal Statistical Society: Series D (The Statistician), 52(3): 381--393. <doi:10.1111/1467-9884.00366>.
	"""
	
	cran = "bivpois" 

	version("1.0", md5="735bbbdabcdb427b7fea33e67f783625")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
