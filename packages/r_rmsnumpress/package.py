# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmsnumpress(RPackage):
	"""'Rcpp' Bindings to Native C++ Implementation of MS Numpress

	'Rcpp' bindings to the native C++ implementation of MS Numpress, that provides two compression schemes for numeric data from mass spectrometers. The library provides implementations of 3 different algorithms, 1 designed to compress first order smooth data like retention time or M/Z arrays, and 2 for compressing non smooth data with lower requirements on precision like ion count arrays. Refer to the publication (Teleman et al., (2014) <doi:10.1074/mcp.O114.037879>) for more details.
	"""
	
	cran = "RMSNumpress" 

	version("1.0.1", md5="8302e7b1dacaa007ddf330c18c120c7d")

	depends_on("r-rcpp", type=("build", "run"))
