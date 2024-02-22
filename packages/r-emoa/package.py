# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmoa(RPackage):
	"""Evolutionary Multiobjective Optimization Algorithms

	Collection of building blocks for the design and analysis
        of evolutionary multiobjective optimization algorithms.
	"""
	
	homepage = "https://github.com/olafmersmann/emoa/"
	cran = "emoa" 

	version("0.5-2", md5="9fe18a1e0ddf216faedbc49b2cc0c4a8")

