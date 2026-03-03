# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatt(RPackage):
	"""The Cochran-Armitage Trend Test

	This function conducts the Cochran-Armitage trend test to a 2 by k contingency table. It will report the test statistic (Z) and p-value.A linear trend in the frequencies will be calculated, because the weights (0,1,2) will be used by default. 
	"""
	
	cran = "CATT" 

	version("2.0", md5="d651d67d98c7c95d3c83dbd24d870109")

