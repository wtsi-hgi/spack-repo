# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsonstrings(RPackage):
	"""Manipulation of JSON Strings

	Fast manipulation of JSON strings. Allows to extract or
    delete an element in a JSON string, merge two JSON strings, and more.
	"""
	
	homepage = "https://github.com/stla/jsonStrings"
	cran = "jsonStrings" 

	version("2.1.1", md5="73e8b15b46841e164e4b864d391d362b")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
