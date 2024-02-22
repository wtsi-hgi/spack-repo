# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFree(RPackage):
	"""Flexible Regularized Estimating Equations

	Unified regularized estimating equation solver. Currently the package includes one solver with the l1 penalty only. More solvers and penalties are under development. Reference: Yi Yang, Yuwen Gu, Yue Zhao, Jun Fan (2021) <arXiv:2110.11074>.
	"""
	
	cran = "free" 

	version("1.0.1", md5="9fbec560a499284385ba81cef091a9a1")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
