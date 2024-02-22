# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRzigzag(RPackage):
	"""Zig-Zag Sampler

	Implements the Zig-Zag algorithm (Bierkens, Fearnhead, Roberts, 2016) <arXiv:1607.03188> applied and Bouncy Particle Sampler <arXiv:1510.02451> for a Gaussian target and Student distribution.
	"""
	
	cran = "RZigZag" 

	version("0.2.1", md5="edd38da5d1e30bbd57711ec50aa95f87")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
