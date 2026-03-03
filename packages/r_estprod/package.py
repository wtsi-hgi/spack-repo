# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstprod(RPackage):
	"""Estimation of Production Functions

	Estimation of production functions by the Olley-Pakes, Levinsohn-Petrin and Wooldridge methodologies. 
    The package aims to reproduce the results obtained with the Stata's user written opreg <http://www.stata-journal.com/article.html?article=st0145> and levpet <http://www.stata-journal.com/article.html?article=st0060> commands. 
    The first was originally proposed by Olley, G.S. and Pakes, A. (1996) <doi:10.2307/2171831>.
    The second by Levinsohn, J. and Petrin, A. (2003) <doi:10.1111/1467-937X.00246>.
	And the third by Wooldridge (2009) <doi:10.1016/j.econlet.2009.04.026>.
	"""
	
	cran = "estprod" 

	version("1.2", md5="7072872d84a0b9c6e525a4850e8b4c9f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-gmm", type=("build", "run"))
