# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicroniche(RPackage):
	"""Microbial Niche Measurements

	Measures niche breadth and overlap of microbial taxa from large matrices.
			Niche breadth measurements include Levins' niche breadth (Bn) index, Hurlbert's Bn 
			and Feinsinger's proportional similarity (PS) index. (Feinsinger, P., Spears, E.E.,
			Poole, R.W. (1981) <doi:10.2307/1936664>). Niche overlap measurements include 
			Levin's Overlap (Ludwig, J.A. and Reynolds, J.F. (1988, ISBN:0471832359)) and a Jaccard 
			similarity index of Feinsinger's PS values between taxa pairs, as Proportional Overlap. 
	"""
	
	cran = "MicroNiche" 

	version("1.0.0", md5="e1bbe8e1f7f28aa084f942ab311d970f")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
