# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParallelpc(RPackage):
	"""Paralellised Versions of Constraint Based Causal Discovery
Algorithms

	Parallelise constraint based causality discovery and causal inference methods. The parallelised algorithms in the package will generate the same results as that of the 'pcalg' package but will be much more efficient. 
	"""
	
	cran = "ParallelPC" 

	version("1.2", md5="0586bdc681400b49e813ea49a0c57c8a")

