# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtwbi(RPackage):
	"""Imputation of Time Series Based on Dynamic Time Warping

	Functions to impute large gaps within time series based on Dynamic Time Warping methods. It contains all required functions to create large missing consecutive values within time series and to fill them, according to the paper Phan et al. (2017), <DOI:10.1016/j.patrec.2017.08.019>. Performance criteria are added to compare similarity between two signals (query and reference).
	"""
	
	homepage = "http://mawenzi.univ-littoral.fr/DTWBI/"
	cran = "DTWBI" 

	version("1.1", md5="19581cf3cf8cf5d268eaf9a91571efd4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-lsa", type=("build", "run"))
