# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultirich(RPackage):
	"""Calculate Multivariate Richness via UTC and sUTC

	Functions to calculate Unique Trait Combinations (UTC) and scaled
    Unique Trait Combinations (sUTC) as measures of multivariate richness. The
    package can also calculate beta-diversity for trait richness and can
    partition this into nestedness-related and turnover components. The code
    will also calculate several measures of overlap. See Keyel and Wiegand
    (2016) <doi:10.1111/2041-210X.12558> for more details.
	"""
	
	cran = "multirich" 

	version("2.1.3", md5="ad532c8710ba007596c5c0676e5d0dbf")

