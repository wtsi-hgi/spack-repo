# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtt(RPackage):
	"""Classical Test Theory Functions

	A collection of common test and item analyses from a classical test theory (CTT) framework. Analyses can be applied to both dichotomous and polytomous data. Functions provide reliability analyses (alpha), item statistics, disctractor analyses, disattenuated correlations, scoring routines, and empirical ICCs.
	"""
	
	cran = "CTT" 

	version("2.3.3", md5="fd888c20b95e6e6f697a701bd7025dc1")

