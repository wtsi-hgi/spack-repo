# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrloca(RPackage):
	"""Operations Research LOCational Analysis Models

	Objects and methods to handle and solve the min-sum location problem, also known as Fermat-Weber problem. The min-sum location problem search for a point such that the weighted sum of the distances to the demand points are minimized. See "The Fermat-Weber location problem revisited" by Brimberg, Mathematical Programming, 1, pg. 71-76, 1995. <DOI:10.1007/BF01592245>.
	     General global optimization algorithms are used to solve the problem, along with the adhoc Weiszfeld method, see "Sur le point pour lequel la Somme des distances de n points donnes est minimum", by Weiszfeld, Tohoku Mathematical Journal, First Series, 43, pg. 355-386, 1937 or "On the point for which the sum of the distances to n given points is minimum", by E. Weiszfeld and F. Plastria, Annals of Operations Research, 167, pg. 7-41, 2009. <DOI:10.1007/s10479-008-0352-z>.
	"""
	
	homepage = "http://knuth.uca.es/orloca/"
	cran = "orloca" 

	version("5.6", md5="c79b1d1b239e2284cd63f16b85f48577")

	depends_on("r-png", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
