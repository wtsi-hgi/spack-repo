# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBskyr(RPackage):
	"""Interact with 'Bluesky' Social

	Collect data from and make posts on 'Bluesky' Social
    via the Hypertext Transfer Protocol (HTTP) Application Programming 
    Interface (API), as documented at <https://atproto.com/specs/xrpc>. This 
    further supports broader queries to the Authenticated Transfer (AT) Protocol
    <https://atproto.com/> which 'Bluesky' Social relies on. Data is returned in a
    tidy format and posts can be made using a simple interface.
	"""
	
	homepage = "https://github.com/christopherkenny/bskyr"
	cran = "bskyr" 

	version("0.1.2", md5="e921af05b1307f1165b5dcc13cc4105a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
