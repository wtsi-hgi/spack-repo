# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConake(RPackage):
	"""Continuous Associated Kernel Estimation

	Continuous smoothing of probability density function on a compact or semi-infinite support is performed using four continuous associated kernels: extended beta, gamma, lognormal and reciprocal inverse Gaussian. The cross-validation technique is also implemented for bandwidth selection.
	"""
	
	homepage = "www.r-project.org"
	cran = "Conake" 

	version("1.0.1", md5="8636e613e3a2d13d54d72d0281a654eb")

