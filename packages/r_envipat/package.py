# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvipat(RPackage):
	"""Isotope Pattern, Profile and Centroid Calculation for Mass
Spectrometry

	Fast and very memory-efficient calculation of isotope patterns,
    subsequent convolution to theoretical envelopes (profiles) plus valley
    detection and centroidization or intensoid calculation. Batch processing,
    resolution interpolation, wrapper, adduct calculations and molecular
    formula parsing.
	Loos, M., Gerber, C., Corona, F., Hollender, J., Singer, H. (2015) 
	<doi:10.1021/acs.analchem.5b00941>.
	"""
	
	homepage = "https://www.envipat.eawag.ch/"
	cran = "enviPat" 

	version("2.6", md5="b3bf71eccf0c915ddeadd2e0bfbfa3d5")

