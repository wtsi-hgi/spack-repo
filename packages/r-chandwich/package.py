# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChandwich(RPackage):
	"""Chandler-Bate Sandwich Loglikelihood Adjustment

	Performs adjustments of a user-supplied independence loglikelihood 
    function using a robust sandwich estimator of the parameter covariance 
    matrix, based on the methodology in Chandler and Bate (2007) 
    <doi:10.1093/biomet/asm015>.  This can be used for cluster correlated data 
    when interest lies in the parameters of the marginal distributions or for 
    performing inferences that are robust to certain types of model 
    misspecification.  Functions for profiling the adjusted loglikelihoods are 
    also provided, as are functions for calculating and plotting confidence 
    intervals, for single model parameters, and confidence regions, for pairs 
    of model parameters.  Nested models can be compared using an adjusted 
    likelihood ratio test.
	"""
	
	homepage = "https://paulnorthrop.github.io/chandwich/"
	cran = "chandwich" 

	version("1.1.6", md5="7fe64112018a8c718178ac2f36490c33")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
