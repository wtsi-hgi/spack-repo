# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmanpg(RPackage):
	"""Alternating Manifold Proximal Gradient Method for Sparse PCA

	Alternating Manifold Proximal Gradient Method for Sparse PCA uses the Alternating Manifold Proximal 
    Gradient (AManPG) method to find sparse principal components from a data or covariance matrix. Provides
    a novel algorithm for solving the sparse principal component analysis problem which provides
    advantages over existing methods in terms of efficiency and convergence guarantees.
    Chen, S., Ma, S., Xue, L., & Zou, H. (2020) <doi:10.1287/ijoo.2019.0032>.
    Zou, H., Hastie, T., & Tibshirani, R. (2006) <doi:10.1198/106186006X113430>.
    Zou, H., & Xue, L. (2018) <doi:10.1109/JPROC.2018.2846588>.
	"""
	
	cran = "amanpg" 

	version("0.3.4", md5="f53e16f3b2f73906d84086d16434a75f")

	depends_on("r@3.5:", type=("build", "run"))
