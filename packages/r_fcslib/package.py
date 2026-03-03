# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcslib(RPackage):
	"""A Collection of Fluorescence Fluctuation Spectroscopy Analysis
Methods

	
    This is a package for fluorescence fluctuation spectroscopy data analysis methods such as spFCS, FCCS, scanning-FCS, pCF, N&B and pCOMB, among others.
    In addition, several data detrending tools are provided. For an extensive user's guide for the use of FCSlib, please navigate to (<https://github.com/FCSlib/FCSlib/tree/master/Documentation>).
    Sample data can be found at (<https://github.com/FCSlib/FCSlib/tree/master/Sample%20Data>).
    The original paper where this package is presented can be found at (<doi:10.1093/bioinformatics/btaa876>).
	"""
	
	cran = "FCSlib" 

	version("1.3.0", md5="c0f2e0e9b13e6e692ba8ee5629fbd31d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
