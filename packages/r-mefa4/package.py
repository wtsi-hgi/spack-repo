# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMefa4(RPackage):
	"""Multivariate Data Handling with S4 Classes and Sparse Matrices

	An S4 update of the 'mefa' package
  using sparse matrices for enhanced efficiency.
  Sparse array-like objects are supported via
  lists of sparse matrices.
	"""
	
	homepage = "https://github.com/psolymos/mefa4"
	cran = "mefa4" 

	version("0.3-9", md5="62809a4ec020b342f76f7cfb5bf5e5ba", url="https://cran.r-project.org/src/contrib/mefa4_0.3-9.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix@1.4.2:", type=("build", "run"))
