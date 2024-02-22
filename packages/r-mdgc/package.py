# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdgc(RPackage):
	"""Missing Data Imputation Using Gaussian Copulas

	Provides functions to impute missing values using Gaussian 
    copulas for mixed data types as described by Christoffersen et al. 
    (2021) <arXiv:2102.02642>. The method is related to Hoff (2007) 
    <doi:10.1214/07-AOAS107> and Zhao and Udell (2019) <arXiv:1910.12845> 
    but differs by making a direct approximation of the log marginal likelihood 
    using an extended version of the Fortran code created by Genz and Bretz 
    (2002) <doi:10.1198/106186002394> in addition to also support multinomial 
    variables.
	"""
	
	homepage = "https://github.com/boennecd/mdgc"
	cran = "mdgc" 

	version("0.1.7", md5="48bc7334208774380defaaa0823643cb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-psqn", type=("build", "run"))
