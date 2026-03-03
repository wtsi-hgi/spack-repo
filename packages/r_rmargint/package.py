# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmargint(RPackage):
	"""Robust Marginal Integration Procedures

	Three robust marginal integration procedures for additive models based on local 
             polynomial kernel smoothers. As a preliminary estimator of the multivariate 
             function for the marginal integration procedure, a first approach uses local 
             constant M-estimators, a second one uses local polynomials of order 1 over all the
             components of covariates, and the third one uses M-estimators based on local 
             polynomials but only in the direction of interest. For this last approach, 
             estimators of the derivatives of the additive functions can be obtained. All three
             procedures can compute predictions for points outside the training set if desired. 
             See Boente and Martinez (2017) <doi:10.1007/s11749-016-0508-0> for details. 
	"""
	
	cran = "rmargint" 

	version("2.0.3", md5="da734fab37bb94d3962ef81bb78bf1ed")

