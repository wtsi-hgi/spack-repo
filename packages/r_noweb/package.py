# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoweb(RPackage):
	"""The 'noweb' System for R

	The noweb system for source code, implemented in R.
	"""
	
	cran = "noweb" 

	version("1.1-4", md5="b69ff503cebc0536b012d265205bd5b3")

