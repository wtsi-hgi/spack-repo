# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmirnov(RPackage):
	"""Provides two taxonomic coefficients from E. S. Smirnov
"Taxonomic analysis" (1969) book

	This tiny package contains one function smirnov() which
        calculates two scaled taxonomic coefficients, Txy (coefficient
        of similarity) and Txx (coefficient of originality). These two
        characteristics may be used for the analysis of similarities
        between any number of taxonomic groups, and also for assessing
        uniqueness of giving taxon. It is possible to use smirnov()
        output as a distance measure: convert it to distance by
        "as.dist(1 - smirnov(x))".
	"""
	
	cran = "smirnov" 

	version("1.0-1", md5="7a668805304099971731281e112e673a")

