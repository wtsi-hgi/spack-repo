# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPassword(RPackage):
	"""Create Random Passwords

	Create random passwords of letters, numbers and punctuation.
	"""
	
	cran = "password" 

	version("1.0-0", md5="82e957a9b3b3f8c286f4078233ea4b20")

