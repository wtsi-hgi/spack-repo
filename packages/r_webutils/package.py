# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebutils(RPackage):
	"""Utility Functions for Developing Web Applications

	Parses http request data in application/json, multipart/form-data, 
    or application/x-www-form-urlencoded format. Includes example of hosting
    and parsing html form data in R using either 'httpuv' or 'Rhttpd'.
	"""
	
	homepage = "https://jeroen.r-universe.dev/webutils"
	cran = "webutils" 

	version("1.2.0", md5="b22bccdb361730d8aa1d7cf2cbd3e9fa")

	depends_on("r-curl@2.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
