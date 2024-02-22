# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuandl(RPackage):
	"""API Wrapper for Quandl.com

	Functions for interacting directly with the Quandl API to offer data in a number of formats usable in R, downloading a zip with all data from a Quandl database, and the ability to search. This R package uses the Quandl API. For more information go to <https://docs.quandl.com>. For more help on the package itself go to <https://www.quandl.com/tools/r>.
	"""
	
	homepage = "https://github.com/quandl/quandl-r"
	cran = "Quandl" 

	version("2.11.0", md5="f113ea24a05ed2affcf385440bfbce07")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-httr@0.6.1:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-jsonlite@0.9.14:", type=("build", "run"))
