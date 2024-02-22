# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFas(RPackage):
	"""Factor-Augmented Sparse Regression Tuning-Free Testing

	The 'FAS' package implements the bootstrap method for the tuning parameter selection and tuning-free inference on sparse regression coefficient vectors. Currently, the test could be applied to linear and factor-augmented sparse regressions, see Lederer & Vogt (2021, JMLR) <https://www.jmlr.org/papers/volume22/20-539/20-539.pdf> and Beyhum & Striaukas (2023) <arXiv:2307.13364>. 
	"""
	
	cran = "FAS" 

	version("1.0.0", md5="d677bbba6eb0e06f9b4b0c75124b8cd7")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
