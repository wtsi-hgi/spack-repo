# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDccpp(RPackage):
	"""Fast Computation of Distance Correlations

	Fast computation of the distance covariance 'dcov' and distance correlation 'dcor'.  The computation cost is only O(n log(n)) for the distance correlation (see Chaudhuri, Hu (2019) <arXiv:1810.11332> <doi:10.1016/j.csda.2019.01.016>). The functions are written entirely in C++ to speed up the computation.
	"""
	
	homepage = "https://dccpp.berrisch.biz/"
	cran = "dccpp" 

	version("0.1.0", md5="50b7a32273b16b643119c7c837c2f317")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
