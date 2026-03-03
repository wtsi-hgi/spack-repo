# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUrlshortener(RPackage):
	"""R Wrapper for the 'Bit.ly' and 'Is.gd'/'v.gd' URL Shortening
Services

	Allows using two URL shortening services, which also provide
    expanding and analytic functions. Specifically developed for 'Bit.ly' (which requires OAuth 2.0) and 'is.gd' (no API key).
	"""
	
	homepage = "https://github.com/dmpe/urlshorteneR"
	cran = "urlshorteneR" 

	version("1.5.7", md5="3d9bc20f9173886f1f13cc785b8cadc1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-httr@1.4.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.8:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-shiny@1.7.2:", type=("build", "run"))
	depends_on("r-clipr@0.8:", type=("build", "run"))
	depends_on("r-miniui@0.1.1.1:", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
