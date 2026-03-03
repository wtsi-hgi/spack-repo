# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgooglefit(RPackage):
	"""R Interface to Google Fit API

	Provides interface to Google Fit REST API v1 (see <https://developers.google.com/fit/rest/v1/reference/>). 
	"""
	
	cran = "RGoogleFit" 

	version("0.4.0", md5="bcc3c329ed1b4d5d5f24655a7b413b2c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
