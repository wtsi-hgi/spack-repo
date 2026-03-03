# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedditextractor(RPackage):
	"""Reddit Data Extraction Toolkit

	A collection of tools for extracting structured data from <https://www.reddit.com/>.
	"""
	
	cran = "RedditExtractoR" 

	version("3.0.9", md5="2fa798c876842f19ada8671715e7e89a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
