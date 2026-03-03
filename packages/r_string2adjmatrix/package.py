# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RString2adjmatrix(RPackage):
	"""Creates an Adjacency Matrix from a List of Strings

	Takes a list of character strings and forms an adjacency matrix for
    the times the specified characters appear together in the strings provided. For
    use in social network analysis and data wrangling. Simple package, comprised of
    three functions.
	"""
	
	cran = "String2AdjMatrix" 

	version("0.1.0", md5="bf2f4c8586adc3cd2637cb8e927cc4b9")

	depends_on("r-stringr", type=("build", "run"))
