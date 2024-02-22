# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBizicount(RPackage):
	"""Bivariate Zero-Inflated Count Models Using Copulas

	Maximum likelihood estimation of copula-based zero-inflated 
    (and non-inflated) Poisson and negative binomial count models. Supports Frank 
    and Gaussian copulas. Allows for mixed margins (e.g., one margin Poisson, the 
    other zero-inflated negative binomial), and several marginal link functions. 
    Built-in methods for publication-quality tables using 'texreg', post-estimation 
    diagnostics using 'DHARMa', and testing for marginal zero-modification
    via <doi:10.1177/0962280217749991>. For information on copula regression for count data, 
    see Genest and Nešlehová (2007) <doi:10.1017/S0515036100014963> as well as 
    Nikoloulopoulos (2013) <doi:10.1007/978-3-642-35407-6_11>. For information on zero-inflated
    count regression generally, see Lambert (1992) <https:www.jstor.org/stable/1269547?origin=crossref>. The author 
    acknowledges support by NSF DMS-1925119 and DMS-212324.
	"""
	
	homepage = "https://github.com/jmniehaus/bizicount"
	cran = "bizicount" 

	version("1.3.2", md5="ee09d37cd88c58b46036b4b591515a62")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-pbivnorm@0.6:", type=("build", "run"))
	depends_on("r-formula@1.2.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-mass@7.3.54:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1.1:", type=("build", "run"))
	depends_on("r-dharma@0.3.4:", type=("build", "run"))
	depends_on("r-texreg@1.37.5:", type=("build", "run"))
