# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparselda(RPackage):
	"""Sparse Discriminant Analysis

	Performs sparse linear discriminant analysis for Gaussians and mixture of Gaussian models.
	"""
	
	homepage = "http://www.imm.dtu.dk/~lhc"
	cran = "sparseLDA" 

	version("0.1-9", md5="da7f8a857481a4fb70e5a7c6f876e3e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
