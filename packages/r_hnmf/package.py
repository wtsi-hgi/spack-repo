# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHnmf(RPackage):
	"""Hierarchical Non-Negative Matrix Factorization

	Hierarchical and single-level non-negative matrix factorization. Several NMF algorithms are available.
	"""
	
	cran = "hNMF" 

	version("1.0", md5="925b189b2b48a5ab652d8e7b5d78c6d9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-rasterimage", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
