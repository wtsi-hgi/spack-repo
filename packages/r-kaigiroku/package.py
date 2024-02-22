# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKaigiroku(RPackage):
	"""Programmatic Access to the API for Japanese Diet Proceedings

	Search and download data from the API for Japanese Diet Proceedings (see the reference at <https://kokkai.ndl.go.jp/api.html>).
	"""
	
	homepage = "https://github.com/amatsuo/kaigiroku"
	cran = "kaigiroku" 

	version("0.5", md5="390dd2c5c74c70b2471a5d4dfccb4740")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
