# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJack(RPackage):
	"""Jack, Zonal, and Schur Polynomials

	Symbolic calculation and evaluation of the Jack polynomials,
    zonal polynomials, and Schur polynomials. Mainly based on Demmel &
    Koev's paper (2006) <doi:10.1090/S0025-5718-05-01780-1>. Zonal
    polynomials and Schur polynomials are particular cases of Jack
    polynomials. Zonal polynomials appear in random matrix theory. Schur
    polynomials appear in the field of combinatorics.
	"""
	
	homepage = "https://github.com/stla/jackR"
	cran = "jack" 

	version("5.3.0", md5="a8e7190e478423431b618a5710348c37")

	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-multicool", type=("build", "run"))
	depends_on("r-mvp", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-qspray", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-spray", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
