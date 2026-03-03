# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighttest(RPackage):
	"""Simultaneous Critical Values for t-Tests in Very High Dimensions

	Implements the method developed by Cao and Kosorok (2011) for the 
    significance analysis of thousands of features in high-dimensional 
    biological studies. It is an asymptotically valid data-driven procedure 
    to find critical values for rejection regions controlling the 
    k-familywise error rate, false discovery rate, and the tail probability 
    of false discovery proportion.
	"""
	
	cran = "highTtest" 

	version("1.3", md5="c1f8650524791e4f933cf637905ef9de")

