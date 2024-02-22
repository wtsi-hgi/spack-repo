# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRifle(RPackage):
	"""Sparse Generalized Eigenvalue Problem

	Implements the algorithms for solving sparse generalized eigenvalue problem by Tan, et. al. (2018). Sparse Generalized Eigenvalue Problem: Optimal Statistical Rates via Truncated Rayleigh Flow.  To appear in Journal of the Royal Statistical Society: Series B. <arXiv:1604.08697>.
	"""
	
	cran = "rifle" 

	version("1.0", md5="8254418579a3f9767807c4ed53a72539")

	depends_on("r-mass", type=("build", "run"))
