# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScalealign(RPackage):
	"""Scale Alignment for Between-Items Multidimensional Rasch Family
Models

	Scale alignment is a new procedure for rescaling dimensions of 
    between-items multidimensional Rasch family models so that dimensions scores
    can be compared directly (Feuerstahler & Wilson, 2019; under review) 
	<doi:10.1111/jedm.12209>. This package includes functions for implementing 
    delta-dimensional alignment (DDA) and logistic regression alignment (LRA) 
    for dichotomous or polytomous data. This function also includes a wrapper 
	for models fit using the 'TAM' package.
	"""
	
	cran = "scaleAlign" 

	version("1.0.0.0", md5="d44caa60691b401adb798bb4d576bfcd")

