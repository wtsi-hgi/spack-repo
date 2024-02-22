# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtika(RPackage):
	"""R Interface to 'Apache Tika'

	Extract text or metadata from over a thousand file types, using Apache Tika <https://tika.apache.org/>. Get either plain text or structured XHTML content. 
	"""
	
	homepage = "https://docs.ropensci.org/rtika/"
	cran = "rtika" 

	version("2.7.0", md5="c9898b4453ec295693640ecf855ccb78")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-sys@2.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
