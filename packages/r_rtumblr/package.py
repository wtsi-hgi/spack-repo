# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtumblr(RPackage):
	"""Collecting and Analyzing 'Tumblr' Data

	An implementation of calls designed to collect 'Tumblr' data via its Application Program Interfaces (API), which can be found at the following URL: <https://www.tumblr.com/docs/en/api/v2>.
	"""
	
	homepage = "https://github.com/schochastics/Rtumblr/"
	cran = "Rtumblr" 

	version("0.1.0", md5="442b8589939ea55d78641c991697c75f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
