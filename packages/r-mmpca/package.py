# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmpca(RPackage):
	"""Integrative Analysis of Several Related Data Matrices

	A generalization of principal component analysis for integrative
  analysis. The method finds principal components that describe single matrices
  or that are common to several matrices. The solutions are sparse. Rank of
  solutions is automatically selected using cross validation. The method is
  described in Kallus et al. (2019) <arXiv:1911.04927>.
	"""
	
	homepage = "https://github.com/cyianor/mmpca"
	cran = "mmpca" 

	version("2.0.3", md5="eb89ac4a93f1489a1371e9695f7fb5e9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-digest@0.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
