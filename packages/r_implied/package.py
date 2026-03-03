# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImplied(RPackage):
	"""Convert Between Bookmaker Odds and Probabilities

	Convert between bookmaker odds and probabilities. Eight different
    algorithms are available, including basic normalization, Shin's method 
    (Hyun Song Shin, (1992) <doi:10.2307/2234526>), and others.
	"""
	
	cran = "implied" 

	version("0.5", md5="f301682b825001ff967676376edc98e2")

