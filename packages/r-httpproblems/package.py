# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttpproblems(RPackage):
	"""Report Errors in Web Applications with 'Problem Details' (RFC
7807)

	Tools for emitting the 'Problem Details' structure defined in
  'RFC' 7807 <https://tools.ietf.org/html/rfc7807> for reporting errors from
  'HTTP' servers in a standard way.
	"""
	
	homepage = "https://github.com/atheriel/httpproblems"
	cran = "httpproblems" 

	version("1.0.1", md5="344f9e6ffd63dd88cb69d08a15008caa")

