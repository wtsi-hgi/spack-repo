# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorbf(RPackage):
	"""Bayesian Tensor Factorization

	Bayesian Tensor Factorization for decomposition of tensor data sets using the trilinear CANDECOMP/PARAFAC (CP) factorization, with automatic component selection. The complete data analysis pipeline is provided, including functions and recommendations for data normalization and model definition, as well as missing value prediction and model visualization. The method performs factorization for three-way tensor datasets and the inference is implemented with Gibbs sampling.
	"""
	
	cran = "tensorBF" 

	version("1.0.2", md5="5841af1bb33fdd5e8ecb6814728cc4c7")

	depends_on("r-tensor", type=("build", "run"))
