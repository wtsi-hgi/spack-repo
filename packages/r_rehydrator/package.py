# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRehydrator(RPackage):
	"""Downloads Tweets from a List of Tweet IDs

	Facilitates replication of Twitter-based research by handling
    common programming tasks needed when downloading tweets.  Specifically, it ensures a 
    user does not exceed Twitter’s rate limits, and it saves tweets in moderately sized files.  
    While a user could perform these tasks in their own code, doing so may be beyond the 
    capabilities of many users.  
	"""
	
	homepage = "https://kevincoakley.github.io/rehydratoR/"
	cran = "rehydratoR" 

	version("0.5.2", md5="c66034e2fb9447b55d4c443507787c46")

	depends_on("r-rtweet@0.6.7:", type=("build", "run"))
	depends_on("r-tibble@1.3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
