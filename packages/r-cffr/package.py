# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCffr(RPackage):
	"""Generate Citation File Format ('cff') Metadata for R Packages

	The Citation File Format version 1.2.0
    <doi:10.5281/zenodo.5171937> is a human and machine readable file
    format which provides citation metadata for software. This package
    provides core utilities to generate and validate this metadata.
	"""
	
	homepage = "https://docs.ropensci.org/cffr/"
	cran = "cffr" 

	version("1.0.0", md5="607ad372d8a132f9000bda68a675e4f2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@2:", type=("build", "run"))
	depends_on("r-desc@1.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-jsonvalidate@1.1:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
