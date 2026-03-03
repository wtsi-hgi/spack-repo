# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwitter(RPackage):
	"""R Based Twitter Client

	Provides an interface to the Twitter web API.
	"""
	
	homepage = "http://lists.hexdump.org/listinfo.cgi/twitter-users-hexdump.org"
	cran = "twitteR" 

	version("1.1.9", md5="7111cf8d04cbb38d33941967d2efadfc")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
