# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytobankapi(RPackage):
	"""Cytobank API Wrapper for R

	Tools to interface with Cytobank's API via R, organized by
    endpoints that represent various areas of Cytobank functionality. Learn more
    about Cytobank at <https://www.beckman.com/flow-cytometry/software>.
	"""
	
	cran = "CytobankAPI" 

	version("2.2.1", md5="582e29acff512c97cde43a71ae101995")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl@2.7:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-aws-s3", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-jose", type=("build", "run"))
