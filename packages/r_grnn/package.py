# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrnn(RPackage):
	"""General regression neural network

	The program GRNN implements the algorithm proposed by
        Specht (1991).
	"""
	
	homepage = "http://flow.chasset.net/r-grnn/"
	cran = "grnn" 

	version("0.1.0", md5="758952c5d4aa27bfd8598b815091b375")

