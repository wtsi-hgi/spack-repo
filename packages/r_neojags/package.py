# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeojags(RPackage):
	"""Neo-Normal Distributions Family for Markov Chain Monte Carlo
(MCMC) Models in 'JAGS'

	A 'JAGS' extension module provides neo-normal distributions
    family including MSNBurr, MSNBurr-IIa, GMSNBurr, Lunetta Exponential Power,
    Fernandez-Steel Skew t, Fernandez-Steel Skew Normal, Fernandez-Osiewalski-Steel
    Skew Exponential Power, Jones Skew Exponential Power.
    References:
    Choir, A. S. (2020). "The New Neo-Normal Distributions and Their Properties".Unpublished Dissertation.
    Denwood, M.J. (2016) <doi:10.18637/jss.v071.i09>.
    Fernandez, C., Osiewalski, J., & Steel, M. F. (1995) <doi:10.1080/01621459.1995.10476637>.
    Fernandez, C., & Steel, M. F. (1998) <doi:10.1080/01621459.1998.10474117>.
    Iriawan, N. (2000). "Computationally Intensive Approaches to Inference in NeoNormal Linear Models".Unpublished Dissertation.
    Mineo, A., & Ruggieri, M. (2005) <doi:10.18637/jss.v012.i04>.
    Rigby, R. A., & Stasinopoulos, D. M. (2005) <doi:10.1111/j.1467-9876.2005.00510.x>.
    Lunetta, G. (1963). "Di una Generalizzazione dello Schema della Curva Normale".
    Rigby, R. A., Stasinopoulos, M. D., Heller, G. Z., & Bastiani, F. D. (2019) <doi:10.1201/9780429298547>.
	"""
	
	homepage = "https://github.com/madsyair/neojags"
	cran = "neojags" 

	version("0.1.4", md5="2ac77836bab37e5e120943d9247ad0f2")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
