# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPiton(RPackage):
	"""Parsing Expression Grammars in Rcpp

	A wrapper around the 'Parsing Expression Grammar Template Library', a C++11 library for generating
    Parsing Expression Grammars, that makes it accessible within Rcpp. With this, developers can implement
    their own grammars and easily expose them in R packages.
	"""
	
	homepage = "https://github.com/Ironholds/piton"
	cran = "piton" 

	version("1.0.0", md5="8b4cd824d0a7a78f93e12f5b18a8df3f")

	depends_on("r-rcpp", type=("build", "run"))
