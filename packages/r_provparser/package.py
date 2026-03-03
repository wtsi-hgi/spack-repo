# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProvparser(RPackage):
	"""Pulls Information from Prov.Json Files

	R functions to access provenance information collected by 'rdt' or 
    'rdtLite'.  The information is stored inside a 'ProvInfo' object and can be 
    accessed through a collection of functions that will return the requested 
    data. The exact format of the JSON created by 'rdt' and 'rdtLite' is described 
    in <https://github.com/End-to-end-provenance/ExtendedProvJson>.
	"""
	
	homepage = "https://github.com/End-to-end-provenance"
	cran = "provParseR" 

	version("1.0", md5="5055ea270449431a9b1b50763c499184")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
