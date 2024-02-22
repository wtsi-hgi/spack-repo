# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsrfa(RPackage):
	"""Non-Supervised Regional Frequency Analysis

	A collection of statistical tools for objective (non-supervised) applications 
             of the Regional Frequency Analysis methods in hydrology. 
             The package refers to the index-value method and, more precisely, helps the
             hydrologist to: (1) regionalize the index-value; (2) form homogeneous regions 
             with similar growth curves; (3) fit distribution functions to the 
             empirical regional growth curves.
             Most of the methods are those described in the Flood Estimation Handbook 
            (Centre for Ecology & Hydrology, 1999, ISBN:9781906698003).
             Homogeneity tests from Hosking and Wallis (1993) <doi:10.1029/92WR01980> 
             and Viglione et al. (2007) <doi:10.1029/2006WR005095> are available.
	"""
	
	cran = "nsRFA" 

	version("0.7-16", md5="2d4abab4872ed0f422a5d4bd21d9f99f")

	depends_on("r@3:", type=("build", "run"))
