# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppbigintalgos(RPackage):
	"""Factor Big Integers with the Parallel Quadratic Sieve

	Features the multiple polynomial quadratic sieve (MPQS) algorithm
    for factoring large integers and a vectorized factoring function that
    returns the complete factorization of an integer. The MPQS is based off of
    the seminal work of Carl Pomerance (1984) <doi:10.1007/3-540-39757-4_17>
    along with the modification of multiple polynomials introduced by Peter
    Montgomery and J. Davis as outlined by Robert D. Silverman (1987)
    <doi:10.1090/S0025-5718-1987-0866119-8>. Utilizes the C library
    GMP (GNU Multiple Precision Arithmetic). For smaller integers, a simple
    Elliptic Curve algorithm is attempted followed by a constrained version of 
    Pollard's rho algorithm. The Pollard's rho algorithm is the same algorithm
    used by the factorize function in the 'gmp' package.
	"""
	
	homepage = "https://github.com/jwood000/RcppBigIntAlgos"
	cran = "RcppBigIntAlgos" 

	version("1.1.0", md5="710d28d235586eb12d209f40fde39360")

	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("gmp@4.2.3:", type=("build", "link", "run"))
