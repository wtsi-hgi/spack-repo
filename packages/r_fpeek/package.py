# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpeek(RPackage):
	"""Check Text Files Content at a Glance

	Tools to help text files importation. It can return 
 the number of lines; print the first and last lines; convert 
 encoding. Operations are made without reading the entire file 
 before starting, resulting in good performances with large files. 
 This package provides an alternative to a simple use of the 
 'head', 'tail', 'wc' and 'iconv' programs that are not always 
 available on machine where R is installed.
	"""
	
	homepage = "https://github.com/davidgohel/fpeek"
	cran = "fpeek" 

	version("0.1.2", md5="7a3641d5d6e74bdcfce564374e4c9c32")

	depends_on("r-rcpp", type=("build", "run"))
