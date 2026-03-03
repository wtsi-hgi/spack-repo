# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRifs(RPackage):
	"""Random Iterated Function System

	Pointwise generation and display of attractors (prefractals) of the random iterated function system (RIFS) for various combinations of probabilistic and geometric parameters of some fixed point sets (protofractals), described by Bukhovets A.G. (2012) <doi:10.1134/S0005117912020154>.
	"""
	
	cran = "RIFS" 

	version("0.1.6", md5="3752d4d83a8da5f120de00ee4d9e36d9")

