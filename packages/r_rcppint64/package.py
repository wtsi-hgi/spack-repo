# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppint64(RPackage):
	"""'Rcpp'-Based Helper Functions to Pass 'Int64' and 'nanotime'
Values Between 'R' and 'C++'

	'Int64' values can be created and accessed via the 'bit64' package and its 'integer64'
 class which package the 'int64' representation cleverly into a 'double'. The 'nanotime' packages
 builds on this to support nanosecond-resolution timestamps. This packages helps conversions between
 'R' and 'C++' via several helper functions provided via a single header file.  A complete example
 client package is included as an illustration.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppint64"
	cran = "RcppInt64" 

	version("0.0.4", md5="19defdecd82e6d2b8a2aab49b24c8196", url="https://cran.r-project.org/src/contrib/RcppInt64_0.0.4.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
