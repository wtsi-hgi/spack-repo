# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarbonate(RPackage):
	"""Interact with 'carbon.js'

	Create beautiful images of source code using
    'carbon.js'<https://carbon.now.sh/about>.
	"""
	
	homepage = "https://github.com/yonicd/carbonate"
	cran = "carbonate" 

	version("0.1.4", md5="b636b6597dff32428f66f6d207c6484e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-details", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rselenium", type=("build", "run"))
	depends_on("r-rtweet", type=("build", "run"))
	depends_on("r-wdman", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
