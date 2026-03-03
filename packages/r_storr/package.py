# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStorr(RPackage):
	"""Simple Key Value Stores

	Creates and manages simple key-value stores.  These can
    use a variety of approaches for storing the data.  This package
    implements the base methods and support for file system, in-memory
    and DBI-based database stores.
	"""
	
	homepage = "https://github.com/richfitz/storr"
	cran = "storr" 

	version("1.2.5", md5="0bec8b9e53ad575bd9a20b68a798f853")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6@2.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
