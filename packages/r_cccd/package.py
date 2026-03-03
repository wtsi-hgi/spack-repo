# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCccd(RPackage):
	"""Class Cover Catch Digraphs

	Class Cover Catch Digraphs, neighborhood graphs, and
        relatives.
	"""
	
	cran = "cccd" 

	version("1.6", md5="4b079ebe359fd114738acf720a455a97")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
