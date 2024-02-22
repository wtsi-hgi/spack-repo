# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMychisq(RPackage):
	"""Chi-Squared Test for Goodness of Fit and Independence Test

	The chi-squared test for goodness of fit 
    and independence test.
	"""
	
	cran = "Mychisq" 

	version("0.1.3", md5="1dc4c97a06981c76901c0c4d2d0a502b")

