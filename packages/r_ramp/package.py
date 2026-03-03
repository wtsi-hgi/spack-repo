# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamp(RPackage):
	"""Regularized Generalized Linear Models with Interaction Effects

	Provides an efficient procedure for fitting the entire solution
    path for high-dimensional regularized quadratic generalized linear models with
    interactions effects under the strong or weak heredity constraint.
	"""
	
	cran = "RAMP" 

	version("2.0.2", md5="556708ad09c1a74186497e80467294ca")

