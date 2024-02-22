# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoortweet(RPackage):
	"""Coordinated Networks Detection on Social Media

	Detects a variety of coordinated actions on social media and outputs the network of coordinated users along with related information.
	"""
	
	homepage = "https://github.com/nicolarighetti/CooRTweet"
	cran = "CooRTweet" 

	version("2.0.0", md5="76564563503330d784a687c817c4be93")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidytable", type=("build", "run"))
	depends_on("r-rcppsimdjson", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
