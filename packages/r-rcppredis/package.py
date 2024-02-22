# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppredis(RPackage):
	"""'Rcpp' Bindings for 'Redis' using the 'hiredis' Library

	Connection to the 'Redis' key/value store using the
 C-language client library 'hiredis' (included as a fallback) with
 'MsgPack' encoding provided via 'RcppMsgPack' headers. It now also
 includes the pub/sub functions from the 'rredis' package.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppredis"
	cran = "RcppRedis" 

	version("0.2.4", md5="6bbc222d0c341c75ffc5edcb9c55ae3f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rapiserialize", type=("build", "run"))
	depends_on("hiredis", type=("build", "link", "run"))
