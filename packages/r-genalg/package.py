# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenalg(RPackage):
	"""R Based Genetic Algorithm

	R based genetic algorithm for binary and floating point
        chromosomes.
	"""
	
	cran = "genalg" 

	version("0.2.1", md5="6677e43553558816799b33d10163c09d")

