# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasttime(RPackage):
	"""Fast Utility Function for Time Parsing and Conversion

	Fast functions for timestamp
	manipulation that avoid system calls and take shortcuts
	to facilitate operations on very large data.
	"""
	
	homepage = "http://www.rforge.net/fasttime"
	cran = "fasttime" 

	version("1.1-0", md5="3a05cbf0e7099c9cc26058c80284336e")

