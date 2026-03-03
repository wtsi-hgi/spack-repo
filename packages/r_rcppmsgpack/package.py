# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppmsgpack(RPackage):
	"""'MsgPack' C++ Header Files and Interface Functions for R

	'MsgPack' header files are provided for use by R packages, along 
 with the ability to access, create and alter 'MsgPack' objects directly from R.
 'MsgPack' is an efficient binary serialization format. It lets you exchange
 data among multiple languages like 'JSON' but it is faster and smaller.
 Small integers are encoded into a single byte, and typical short strings
 require only one extra byte in addition to the strings themselves. This
 package provides headers from the 'msgpack-c' implementation for C and
 C++(11) for use by R, particularly 'Rcpp'. The included 'msgpack-c' headers
 are licensed under the Boost Software License (Version 1.0); the code added
 by this package as well the R integration are licensed under the GPL (>= 2).
 See the files 'COPYRIGHTS' and 'AUTHORS' for a full list of  copyright holders
 and contributors to 'msgpack-c'.  
	"""
	
	cran = "RcppMsgPack" 

	version("0.2.3", md5="021feb04f6c475c426ef46f008451760")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
