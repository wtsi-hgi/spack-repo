# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrfdepth(RPackage):
	"""Depth Measures in Multivariate, Regression and Functional
Settings

	Tools to compute depth measures and implementations of related 
             tasks such as outlier detection, data exploration and 
            classification of multivariate, regression and functional data.
	"""
	
	cran = "mrfDepth" 

	version("1.0.16", md5="29e232060b1704ac9561772f0aac22bd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp@0.12.6:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.2.9:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
