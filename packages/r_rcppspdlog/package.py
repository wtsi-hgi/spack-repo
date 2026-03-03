# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppspdlog(RPackage):
	"""R and C++ Interfaces to 'spdlog' C++ Header Library for Logging

	The mature and widely-used C++ logging library 'spdlog' by Gabi Melman provides
 many desirable features. This package bundles these header files for easy use by R packages
 from both their R and C or C++ code. Explicit use via 'LinkingTo:' is also supported. Also
 see the 'spdl' package which enhanced this package with a consistent R and C++ interface.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppspdlog"
	cran = "RcppSpdlog" 

	version("0.0.16", md5="0604c024744c2a8e4f4979adc65b5a5c")

	depends_on("r-rcpp", type=("build", "run"))
