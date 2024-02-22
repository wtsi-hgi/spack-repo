# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppstreams(RPackage):
	"""'Rcpp' Integration of the 'Streamulus' 'DSEL' for Stream
Processing

	The 'Streamulus' (template, header-only) library by
 Irit Katriel (at <https://github.com/iritkatriel/streamulus>)
 provides a very powerful yet convenient framework for stream
 processing. This package connects 'Streamulus' to R by providing 
 both the header files and all examples.
	"""
	
	homepage = "http://dirk.eddelbuettel.com/code/rcpp.streams.html"
	cran = "RcppStreams" 

	version("0.1.3", md5="8afdee1f7d43fc697eb1241473319a35")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
