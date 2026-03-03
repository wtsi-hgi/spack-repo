# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtoot(RPackage):
	"""Collecting and Analyzing Mastodon Data

	An implementation of calls designed to collect and organize Mastodon data via its Application Program Interfaces (API), which can be found at the following URL: <https://docs.joinmastodon.org/>.
	"""
	
	homepage = "https://gesistsa.github.io/rtoot/"
	cran = "rtoot" 

	version("0.3.4", md5="26741ea6fa629dbc1c4338f27217d1ee")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
