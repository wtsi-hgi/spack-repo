# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGramevol(RPackage):
	"""Grammatical Evolution for R

	A native R implementation of grammatical evolution (GE).
    GE facilitates the discovery of programs that can achieve a desired goal.
    This is done by performing an evolutionary optimisation over a population
    of R expressions generated via a user-defined context-free grammar (CFG)
    and cost function.
	"""
	
	homepage = "https://github.com/fnoorian/gramEvol/"
	cran = "gramEvol" 

	version("2.1-4", md5="150643f56df5561cf7dde30aec85f60d")

