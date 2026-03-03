# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothtensor(RPackage):
	"""A Collection of Smooth Tensor Estimation Methods

	A list of methods for estimating a smooth tensor with an unknown permutation. It also contains several multi-variate functions for generating permuted signal tensors and corresponding observed tensors. For a detailed introduction for the model and estimation techniques, see the paper by Chanwoo Lee and Miaoyan Wang (2021) "Smooth tensor estimation with unknown permutations" <arXiv:2111.04681>.
	"""
	
	homepage = "https://arxiv.org/abs/2111.04681"
	cran = "SmoothTensor" 

	version("0.1.1", md5="56af413d2d8f71c9f4911751d870d3f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
