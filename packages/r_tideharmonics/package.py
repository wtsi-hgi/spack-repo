# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTideharmonics(RPackage):
	"""Harmonic Analysis of Tides

	Implements harmonic analysis of tidal and sea-level data.
  Over 400 harmonic tidal constituents can be estimated, all with 
  daily nodal corrections. Time-varying mean sea-levels can also
  be used.
	"""
	
	cran = "TideHarmonics" 

	version("0.1-1", md5="836eaa2701cb09d95094fd4568da9012")

	depends_on("r@2.10:", type=("build", "run"))
