# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsesvd(RPackage):
	"""Sparse Truncated Singular Value Decomposition (from 'SVDLIBC')

	Wrapper around the 'SVDLIBC' library for (truncated) singular value decomposition of a sparse matrix.
             Currently, only sparse real matrices in Matrix package format are supported.
	"""
	
	homepage = "https://github.com/lucasmaystre/svdlibc"
	cran = "sparsesvd" 

	version("0.2-2", md5="d4e8f508c05c4ddf26031e6da48b8591")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix@1.3:", type=("build", "run"))
