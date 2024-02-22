# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTurner(RPackage):
	"""Turn vectors and lists of vectors into indexed structures

	Package designed for working with vectors and lists of vectors,
    mainly for turning them into other indexed data structures.
	"""
	
	homepage = "http://www.gastonsanchez.com"
	cran = "turner" 

	version("0.1.7", md5="d8c3cda5f3e61b5fa28718c9d0811976")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-tester", type=("build", "run"))
