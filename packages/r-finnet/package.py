# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinnet(RPackage):
	"""Quickly Build and Manipulate Financial Networks

	Providing classes, methods, and functions to deal with financial networks. 
    Users can easily store information about both physical and legal persons by using pre-made classes that are studied for integration with scraping packages such as 'rvest' and 'RSelenium'.
    Moreover, the package assists in creating various types of financial networks depending on the type of relation between its units depending on the relation under scrutiny (ownership, board interlocks, etc.), the desired tie type (valued or binary), and renders them in the most common formats (adjacency matrix, incidence matrix, edge list, 'igraph', 'network').
	"""
	
	homepage = "https://fatelarico.github.io/FinNet.html"
	cran = "FinNet" 

	version("0.1.2", md5="2f8f77b0684bcc7184462e3bb3222224")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
