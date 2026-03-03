# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaschsampler(RPackage):
	"""Rasch Sampler

	MCMC based sampling of binary matrices with fixed margins as used in exact Rasch model tests. 
	"""
	
	cran = "RaschSampler" 

	version("0.8-10", md5="25aed6e623e18adaf6f0e564b8c894b6")

	depends_on("r@4:", type=("build", "run"))
