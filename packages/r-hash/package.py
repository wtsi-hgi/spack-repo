# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHash(RPackage):
	"""Full Featured Implementation of Hash Tables/Associative
Arrays/Dictionaries

	Implements a data structure similar to hashes in Perl and dictionaries in Python but with a purposefully R flavor. For objects of appreciable size, access using hashes outperforms native named lists and vectors.
	"""
	
	homepage = "http://www.johnhughes.org"
	cran = "hash" 

	version("2.2.6.3", md5="69665bf3e3706b0186b585a3537878d2")

	depends_on("r@2.12:", type=("build", "run"))
