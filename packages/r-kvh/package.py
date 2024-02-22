# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKvh(RPackage):
	"""Read/Write Files in Key-Value-Hierarchy Format

	The format KVH is a lightweight format that can be read/written both by humans and machines.
   It can be useful in situations where XML or alike formats seem to be an overkill.
   We provide an ability to parse KVH files in R pretty fast due to 'Rcpp' use.
	"""
	
	homepage = "http://serguei.sokol.free.fr/kvh-format/"
	cran = "kvh" 

	version("1.4.2", md5="82a0c641d556d20246c38ea6ade5feda")

	depends_on("r-rcpp", type=("build", "run"))
