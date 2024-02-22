# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProdest(RPackage):
	"""Production Function Estimation

	Implements the methods proposed by Olley, G.S. and Pakes, A. (1996) <doi:10.2307/2171831>, Levinsohn, J. and Petrin, A. (2003) <doi:10.1111/1467-937X.00246>, Ackerberg, D.A. and Caves, K. and Frazer, G. (2015) <doi:10.3982/ECTA13408> and Wooldridge, J.M. (2009) <doi:10.1016/j.econlet.2009.04.026> for structural productivity estimation .
	"""
	
	homepage = "https://github.com/GabrieleRovigatti/prodest/tree/master/prodest"
	cran = "prodest" 

	version("1.0.1", md5="0753203ef49cd3995e3ef0af852907d0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
