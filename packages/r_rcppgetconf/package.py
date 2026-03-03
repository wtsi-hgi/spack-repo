# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppgetconf(RPackage):
	"""'Rcpp' Interface for Querying System Configuration Variables

	The 'getconf' command-line tool provided by 'libc' allows
 querying of a large number of system variables. This package provides
 similar functionality.
	"""
	
	homepage = "http://dirk.eddelbuettel.com/code/rcpp.getconf.html"
	cran = "RcppGetconf" 

	version("0.0.3", md5="3c9ca01bc4f97accd9369968a0c2c057")

	depends_on("r-rcpp", type=("build", "run"))
