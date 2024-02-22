# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPh2mult(RPackage):
	"""Phase II Clinical Trial Design for Multinomial Endpoints

	Provide multinomial design methods under intersection-union test (IUT) and union-intersection test (UIT) scheme for Phase II trial. The design types include : Minimax (minimize the maximum sample size), Optimal (minimize the expected sample size), Admissible (minimize the Bayesian risk) and Maxpower (maximize the exact power level).
	"""
	
	cran = "ph2mult" 

	version("0.1.1", md5="9862323a1cba68b4fcdd783035a8eef3")

	depends_on("r-clinfun", type=("build", "run"))
