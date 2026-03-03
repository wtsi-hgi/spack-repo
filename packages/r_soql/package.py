# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoql(RPackage):
	"""Helps Make Socrata Open Data API Calls

	Used to construct the URLs and parameters of 'Socrata Open Data API' <https://dev.socrata.com> calls, using the API's 'SoQL' parameter format. Has method-chained and sensical syntax. Plays well with pipes.
	"""
	
	cran = "soql" 

	version("0.1.1", md5="5e4088355309dce08b0f3ca408a66c46")

