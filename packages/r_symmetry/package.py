# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymmetry(RPackage):
	"""Testing for Symmetry of Data and Model Residuals

	Implementations of a large number of tests for symmetry and their 
    bootstrap variants, which can be used for testing the symmetry of random
    samples around a known or unknown mean. Functions are also there for testing
    the symmetry of model residuals around zero. Currently, the supported models
    are linear models and generalized autoregressive conditional
    heteroskedasticity (GARCH) models (fitted with the 'fGarch' package). All
    tests are implemented using the 'Rcpp' package which ensures great
    performance of the code.
	"""
	
	cran = "symmetry" 

	version("0.2.3", md5="e6e6300f77c09122de912e26db935d44")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
