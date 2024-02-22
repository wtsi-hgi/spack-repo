# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGips(RPackage):
	"""Gaussian Model Invariant by Permutation Symmetry

	Find the permutation symmetry group such that the covariance
    matrix of the given data is approximately invariant under it.
    Discovering such a permutation decreases the number of observations
    needed to fit a Gaussian model, which is of great use when it is
    smaller than the number of variables. Even if that is not the case,
    the covariance matrix found with 'gips' approximates the actual
    covariance with less statistical error. The methods implemented in
    this package are described in Graczyk et al. (2022)
    <doi:10.1214/22-AOS2174>.
	"""
	
	homepage = "https://github.com/PrzeChoj/gips"
	cran = "gips" 

	version("1.2.1", md5="1ebef2aa6abeef0077bd165699f4f543")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-permutations", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
