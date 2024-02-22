# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmatr(RPackage):
	"""(Standardised) Major Axis Estimation and Testing Routines

	Methods for fitting bivariate lines in
    allometry using the major axis (MA) or standardised major axis (SMA), and
    for making inferences about such lines. The available methods of inference
    include confidence intervals and one-sample tests for slope and elevation,
    testing for a common slope or elevation amongst several allometric lines,
    constructing a confidence interval for a common slope or elevation, and
    testing for no shift along a common axis, amongst several samples. 
    See Warton et al. 2012 <doi:10.1111/j.2041-210X.2011.00153.x> for methods description.
	"""
	
	homepage = "http://web.maths.unsw.edu.au/~dwarton"
	cran = "smatr" 

	version("3.4-8", md5="61b1d814b07de91043918aea12ca52c0")

