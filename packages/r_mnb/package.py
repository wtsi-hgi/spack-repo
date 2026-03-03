# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnb(RPackage):
	"""Diagnostic Tools for a Multivariate Negative Binomial Model

	Diagnostic tools as residual analysis, global, 
    local and total-local influence for the multivariate model 
    from the random intercept Poisson generalized log gamma model 
    are available in this package. Including also, the estimation 
    process by maximum likelihood method, for details see 
    Fabio, L. F; Villegas, C. L.; Carrasco, J.M.F and de Castro, M. (2021) 
    <doi:10.1080/03610926.2021.1939380>.
	"""
	
	cran = "MNB" 

	version("1.1.0", md5="c28daabb0dd75fa7a13ee847f76c9788")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
