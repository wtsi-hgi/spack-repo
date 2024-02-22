# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlgorithmia(RPackage):
	"""Allows you to Easily Interact with the Algorithmia Platform

	The company, Algorithmia, houses the largest marketplace of online
    algorithms. This package essentially holds a bunch of REST wrappers that
    make it very easy to call algorithms in the Algorithmia platform and access
    files and directories in the Algorithmia data API. To learn more about the
    services they offer and the algorithms in the platform visit
    <http://algorithmia.com>. More information for developers can be found at
    <https://algorithmia.com/developers>.
	"""
	
	cran = "algorithmia" 

	version("0.3.0", md5="29b7d048f67cfad2537ff1dd78927ec4")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
