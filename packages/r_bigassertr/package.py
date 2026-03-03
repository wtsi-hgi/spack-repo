# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigassertr(RPackage):
	"""Assertion and Message Functions

	
    Enhanced message functions (cat() / message() / warning() / error()) 
    using wrappers around sprintf(). Also, multiple assertion functions 
    (e.g. to check class, length, values, files, arguments, etc.).
	"""
	
	homepage = "https://github.com/privefl/bigassertr"
	cran = "bigassertr" 

	version("0.1.6", md5="117e5596df34dc306881809960c2233d")

