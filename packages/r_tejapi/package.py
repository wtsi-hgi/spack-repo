# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTejapi(RPackage):
	"""API Wrapper for Taiwan Economic Journal Data Service

	Functions for interacting directly with the Taiwan Economic Journal API to offer data in R. For more information go to <https://api.tej.com.tw>.
	"""
	
	homepage = "https://api.tej.com.tw"
	cran = "Tejapi" 

	version("1.0.1", md5="000ef8c875becbb102a88587c07330a4")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-httr@0.6.1:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.14:", type=("build", "run"))
