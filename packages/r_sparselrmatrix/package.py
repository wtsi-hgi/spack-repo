# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparselrmatrix(RPackage):
	"""Represent and Use Sparse + Low Rank Matrices

	Provides an S4 class for representing and
    interacting with sparse plus rank matrices. At the moment the
    implementation is quite spare, but the plan is eventually subclass
    Matrix objects.
	"""
	
	homepage = "https://rohelab.github.io/sparseLRMatrix/"
	cran = "sparseLRMatrix" 

	version("0.1.0", md5="5375f75c5a0004c05ca5507b92591a8f")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
