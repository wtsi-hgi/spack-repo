# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgs(RPackage):
	"""Sparse-Group SLOPE: Adaptive Bi-Level Selection with FDR Control

	Implementation of Sparse-group SLOPE: Adaptive bi-level with FDR-control (Feser et al. (2023) <arXiv:2305.09467>). Linear and logistic regression models are supported, both of which can be fit using k-fold cross-validation. Dense and sparse input matrices are supported. In addition, a general adaptive three operator splitting (ATOS) implementation is provided.
	"""
	
	homepage = "https://github.com/ff1201/sgs"
	cran = "sgs" 

	version("0.1.1", md5="88a510b1ba87056f162dd3f42c0f895d")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-faux", type=("build", "run"))
	depends_on("r-slope", type=("build", "run"))
	depends_on("r-rlab", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
