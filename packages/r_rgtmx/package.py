# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgtmx(RPackage):
	"""Manage GTmetrix Tests in R

	This is a library to access the current API of the web speed test service 'GTmetrix'.
    It provides a convenient wrapper to start tests, get reports, and access all kinds of meta data. 
    For more information about using the API please visit <https://gtmetrix.com/api/docs/2.0/>.
	"""
	
	homepage = "https://github.com/RomanAbashin/rgtmx"
	cran = "rgtmx" 

	version("0.1.4", md5="869611aec6949a05f9ca22b484b88c6d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
