# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdering(RPackage):
	"""Test, Check, Verify, Investigate the Monotonic Properties of
Vectors

	Functions to test/check/verify/investigate the ordering of vectors. 
    The 'is_[strictly_]*' family of functions test vectors for 
    'sorted', 'monotonic', 'increasing', 'decreasing' order; 'is_constant' 
    and 'is_incremental' test for the degree of ordering. `ordering` 
    provides a numeric indication of ordering -2 (strictly decreasing) to 
    2 (strictly increasing).
	"""
	
	homepage = "https://github.com/decisionpatterns/ordering"
	cran = "ordering" 

	version("0.7.0", md5="f45197a3fd23d098d94cef49bb68311e")

