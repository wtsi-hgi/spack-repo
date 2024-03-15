# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeoptimr(RPackage):
	"""Differential Evolution Optimization in Pure R.

	Differential Evolution (DE) stochastic algorithms for global optimization
	of problems with and without constraints. The aim is to curate a collection
	of its state-of-the-art variants that (1) do not sacrifice simplicity of
	design, (2) are essentially tuning-free, and (3) can be efficiently
	implemented directly in the R language. Currently, it only provides an
	implementation of the 'jDE' algorithm by Brest et al. (2006)
	<doi:10.1109/TEVC.2006.872133>."""

	cran = "DEoptimR"

	version("1.1-3", md5="945667c3199760a35837e0a1b72f3648")

