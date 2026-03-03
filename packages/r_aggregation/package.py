# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAggregation(RPackage):
	"""p-Value Aggregation Methods

	Contains functionality for performing the following methods of p-value aggregation: Fisher's method [Fisher, RA (1932, ISBN: 9780028447308)], the Lancaster method (weighted Fisher's method) [Lancaster, HO (1961, <doi:10.1111/j.1467-842X.1961.tb00058.x>)], and Sidak correction [Sidak, Z (1967, <doi:10.1080/01621459.1967.10482935>)].  Please cite Yi et al., the manuscript corresponding to this package [Yi, L et al., (2017), <doi:10.1101/190199>].
	"""
	
	cran = "aggregation" 

	version("1.0.1", md5="ef514bc6eee647289efd96b46dd26e98")

