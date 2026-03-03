# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphtweets(RPackage):
	"""Visualise Twitter Interactions

	Allows building an edge table from data frame of tweets, 
  also provides function to build nodes and another create a temporal graph.
	"""
	
	homepage = "http://graphTweets.john-coene.com"
	cran = "graphTweets" 

	version("0.5.3", md5="e99873f33b15135226e9be29282a67a6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
