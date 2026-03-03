# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsemvn(RPackage):
	"""Multivariate Normal Functions for Sparse Covariance and
Precision Matrices

	Computes multivariate normal (MVN) densities, and
    samples from MVN distributions, when the covariance or
    precision matrix is sparse.
	"""
	
	homepage = "https://braunm.github.io/sparseMVN/"
	cran = "sparseMVN" 

	version("0.2.2", md5="003e34ff41b43403ba6a4a4e2a822bbb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix@1.3:", type=("build", "run"))
