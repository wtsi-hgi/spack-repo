# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgoogleslides(RPackage):
	"""R Interface to Google Slides

	Previously, when one is working with in the Google Ecosystem (Using Google Drive etc), there is hardly any good workflow of getting the values calculated from R and getting that into Google Slides. The normal and easy way out would be to just copy your work over but when you have a number of analysis to present with a lot of changes between each environment, it just becomes quite cumbersome.
	"""
	
	cran = "rgoogleslides" 

	version("0.3.2", md5="cc1a01742f5bf746715b593b29ee267c")

	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
