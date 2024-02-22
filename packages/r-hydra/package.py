# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydra(RPackage):
	"""Hyperbolic Embedding

	Calculate an optimal embedding of a set of data points into low-dimensional hyperbolic space. This uses the strain-minimizing hyperbolic embedding of Keller-Ressel and Nargang (2019), see <arXiv:1903.08977>. 
	"""
	
	cran = "hydra" 

	version("0.1.0", md5="3bdb3abeaf831ad2dd81ba4350febfda")

