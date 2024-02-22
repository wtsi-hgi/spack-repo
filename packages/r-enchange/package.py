# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnchange(RPackage):
	"""Ensemble Methods for Multiple Change-Point Detection

	Implements a segmentation algorithm for multiple change-point detection in univariate time series using the Ensemble Binary Segmentation of Korkas (2020) <arXiv:2003.03649>.
	"""
	
	cran = "eNchange" 

	version("1.0", md5="1c633e405e640be2fe40cdd3bb251129")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-hawkes", type=("build", "run"))
	depends_on("r-acdm", type=("build", "run"))
