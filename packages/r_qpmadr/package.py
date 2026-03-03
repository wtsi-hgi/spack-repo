# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQpmadr(RPackage):
	"""Interface to the 'qpmad' Quadratic Programming Solver

	Efficiently solve quadratic problems with linear inequality, equality and box constraints. The method used is outlined in D. Goldfarb, and A. Idnani (1983) <doi:10.1007/BF02591962>.
	"""
	
	homepage = "https://github.com/anderic1/qpmadr"
	cran = "qpmadr" 

	version("1.1.0-0", md5="f0c24592ce94d67776ea8c7d4e55c81e")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
