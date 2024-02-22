# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNasdaqdatalink(RPackage):
	"""API Wrapper for Nasdaq Data Link

	Functions for interacting directly with the Nasdaq Data Link API to offer data in a number of formats usable in R, downloading a zip with all data from a Nasdaq Data Link database, and the ability to search. This R package uses the Nasdaq Data Link API. For more information go to <https://docs.data.nasdaq.com/>. For more help on the package itself go to <https://data.nasdaq.com/tools/r>.
	"""
	
	homepage = "https://github.com/nasdaq/data-link-r"
	cran = "NasdaqDataLink" 

	version("1.0.0", md5="f0c17b6e54e2e077b68623289af5cb4f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-httr@0.6.1:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-jsonlite@0.9.14:", type=("build", "run"))
