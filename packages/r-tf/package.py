# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTf(RPackage):
	"""S3 Classes and Methods for Tidy Functional Data

	Defines S3 vector data types for vectors of functional data 
   (grid-based, spline-based or functional principal components-based) with all 
   arithmetic and summary methods, derivation, integration and smoothing, 
   plotting, data import and export, and data wrangling, such as re-evaluating, 
   subsetting, sub-assigning, zooming into sub-domains, or extracting functional 
   features like minima/maxima and their locations. 
   The implementation allows including such vectors in data frames for joint 
   analysis of functional and scalar variables.
	"""
	
	homepage = "https://tidyfun.github.io/tf/"
	cran = "tf" 

	version("0.3.3", md5="341ed9083c65484219bd5e16616dcf63")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs@0.2.4:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
