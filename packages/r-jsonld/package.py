# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsonld(RPackage):
	"""JSON for Linking Data

	JSON-LD is a light-weight syntax for expressing linked data. It is primarily
    intended for web-based programming environments, interoperable web services and for 
    storing linked data in JSON-based databases. This package provides bindings to the 
    JavaScript library for converting, expanding and compacting JSON-LD documents.
	"""
	
	homepage = "https://docs.ropensci.org/jsonld"
	cran = "jsonld" 

	version("2.2", md5="7ba93bfd54aa1e2e241eef1d0073b3cd")

	depends_on("r-v8", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl@2.7:", type=("build", "run"))
