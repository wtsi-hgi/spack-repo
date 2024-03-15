# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXxhashlite(RPackage):
	"""Extremely Fast Hashing of R Objects, Raw Data and Files using
'xxHash' Algorithms

	Extremely fast hashing of R objects using 'xxHash'.  R objects are hashed via
    the standard serialization mechanism in R.  Raw byte vectors and strings
    can be handled directly for compatibility with hashes created on 
    other systems.  This implementation is a wrapper around the 'xxHash' 'C'
    library which is available from <https://github.com/Cyan4973/xxHash>.
	"""
	
	homepage = "https://github.com/coolbutuseless/xxhashlite"
	cran = "xxhashlite" 

	version("0.2.2", md5="3ed21677c9a3061109986fef70673ee0")

	depends_on("r@3.5:", type=("build", "run"))
