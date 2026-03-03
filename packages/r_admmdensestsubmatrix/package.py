# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmmdensestsubmatrix(RPackage):
	"""Alternating Direction Method of Multipliers to Solve Dense
Dubmatrix Problem

	Solves the problem of identifying the densest submatrix in a given or sampled binary matrix, Bombina et al. (2019) <arXiv:1904.03272>.
	"""
	
	cran = "admmDensestSubmatrix" 

	version("0.1.0", md5="f68b49b4543b31ea0802bbe5f7872fc7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
