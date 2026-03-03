# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShiftr(RPackage):
	"""Fast Enrichment Analysis via Circular Permutations

	Fast enrichment analysis for locally correlated statistics
        via circular permutations.
        The analysis can be performed at multiple significance thresholds
        for both primary and auxiliary data sets with
        efficient correction for multiple testing.
	"""
	
	homepage = "https://github.com/andreyshabalin/shiftR"
	cran = "shiftR" 

	version("1.5", md5="4f3c7a45ca4b7c38680b9e80ba515319")

