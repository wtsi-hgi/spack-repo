# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixsampling(RPackage):
	"""Simulations of Matrix Variate Distributions

	Provides samplers for various matrix variate distributions: Wishart, inverse-Wishart, normal, t, inverted-t, Beta type I, Beta type II, Gamma, confluent hypergeometric. Allows to simulate the noncentral Wishart distribution without the integer restriction on the degrees of freedom.
	"""
	
	homepage = "https://github.com/stla/matrixsampling"
	cran = "matrixsampling" 

	version("2.0.0", md5="89bbc477239cf0f886af2bc39aac1df5")

	depends_on("r-keep", type=("build", "run"))
