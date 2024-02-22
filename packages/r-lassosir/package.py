# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLassosir(RPackage):
	"""Sparsed Sliced Inverse Regression via Lasso

	Estimate the sufficient dimension reduction space using sparsed sliced inverse regression via Lasso (Lasso-SIR) introduced in Lin, Zhao, and Liu (2017) <arxiv:1611.06655>. The Lasso-SIR is consistent and achieve the optimal convergence rate under certain sparsity conditions for the multiple index models.
	"""
	
	cran = "LassoSIR" 

	version("0.1.1", md5="4d613bbd1b5344f5d02fd229609ab8f6")

	depends_on("r-glmnet", type=("build", "run"))
